# This code is part of Qiskit.
#
# (C) Copyright IBM 2020s.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import bpy
from animation_nodes.base_types import AnimationNode

import numpy as np

seed = 71
np.random.seed = seed

from qiskit import QuantumRegister, QuantumCircuit, BasicAer
# from qiskit.circuit.library import TwoLocal, UniformDistribution #deprecated
from qiskit.circuit.library import TwoLocal

from qiskit_finance.circuit.library import UniformDistribution

from qiskit.utils import QuantumInstance, algorithm_globals
from qiskit_machine_learning.algorithms import NumPyDiscriminator, QGAN

algorithm_globals.random_seed = seed


class RunQGAN(bpy.types.Node, AnimationNode):
    bl_idname = "an_qGAN"
    bl_label = "qGAN Processing"

    # No inputs at the moment, later: input data (mesh, etc.)
    def create(self):
        #self.newInput("Object", "Training Object 1", "trainingObject", defaultDrawType = "PROPERTY_ONLY")

        self.newOutput("Integer", "Nb of Epochs", "numEpochs")  # For G_loss and D_loss, and relative entropy graphs
        # self.newOutput("List", "Bounds", "bounds") # For simulation vs target comparison graph # TO UNCOMMENT
        # To be able to get outputs of the qGAN generator in qgan_histogram.py # TO UNCOMMENT
        self.newOutput("QGAN", "qGAN", "qgan")
        # self.newOutput("Float", "Float test", "testFloat") # DEBUG
        # self.newOutput("Integer", "Integer test", "testInt") # DEBUG
        # self.newOutput("dict_items", "Training Results", "result.items()") # ->
        # To separate in multiple outputs (one for each value of the dict) ; use
        # result.items() instead of variable?
        self.newOutput("Float", "Relative Entropy", "rel_entropy")

    def execute(self):  # , trainingObject

        # Default return values
        # if numEpochs is None or bounds is None:
        # return 0, np.array([0.0, 0.0])
        # if numEpochs is None or qgan is None:
        #     return 0, QGAN([0], np.array([0.0, 0.0]), [0], 1, 0, snapshot_dir=None)

        # ------------- LOAD THE TRAINING DATA --------------

        # Number training data samples
        N = 1000  # Was 1000 before but took too long

        # Load data samples from log-normal distribution with mean=1 and standard deviation=1
        mu = 1
        sigma = 1
        # the mean and standard deviation are not the values for the distribution
        # itself, but of the underlying normal distribution it is derived from
        real_data = np.random.lognormal(mean=mu, sigma=sigma, size=N)

        # Set the data resolution
        # Set upper and lower data values as list of k min/max data values [[min_0,max_0],...,[min_k-1,max_k-1]]
        bounds = np.array([0.0, 3.0])  # the "window" for histogram visualization
        # Set number of qubits per data dimension as list of k qubit values[#q_0,...,#q_k-1]
        num_qubits = [2]
        k = len(num_qubits)

        # ------------- INITIALIZE THE QGAN --------------

        # Set number of training epochs
        # Note: The algorithm's runtime can be shortened by reducing the number of training epochs.
        num_epochs = 10
        # Batch size
        batch_size = 100  # Was 100 before but took too long

        # Initialize qGAN
        qgan = QGAN(real_data, bounds, num_qubits, batch_size, num_epochs, snapshot_dir=None)
        qgan.seed = 1
        # Set quantum instance to run the quantum generator
        quantum_instance = QuantumInstance(
            backend=BasicAer.get_backend("statevector_simulator"), seed_transpiler=seed, seed_simulator=seed
        )

        # Set entangler map
        entangler_map = [[0, 1]]

        # Set an initial state for the generator circuit
        init_dist = UniformDistribution(sum(num_qubits))

        # Set the ansatz circuit
        ansatz = TwoLocal(int(np.sum(num_qubits)), "ry", "cz", entanglement=entangler_map, reps=1)

        # Set generator's initial parameters - in order to reduce the training time and hence the
        # total running time for this notebook
        init_params = [3.0, 1.0, 0.6, 1.6]

        # You can increase the number of training epochs and use random initial parameters.
        # init_params = np.random.rand(ansatz.num_parameters_settable) * 2 * np.pi

        # Set generator circuit by adding the initial distribution infront of the ansatz
        g_circuit = ansatz.compose(init_dist, front=True)

        # Set quantum generator
        qgan.set_generator(generator_circuit=g_circuit, generator_init_params=init_params)
        # The parameters have an order issue that following is a temp. workaround
        qgan._generator._free_parameters = sorted(g_circuit.parameters, key=lambda p: p.name)
        # Set classical discriminator neural network
        discriminator = NumPyDiscriminator(len(num_qubits))
        qgan.set_discriminator(discriminator)

        # ------------- RUN THE QGAN TRAINING --------------
        # Run qGAN
        result = qgan.run(quantum_instance)

        print("Training results:")
        for key, value in result.items():
            print(f"  {key} : {value}")  # Print this data in a viewer node in Blender in addition to Relative Entropy?
            if(key == "rel_entr"):
                rel_entropy = value

        training_results = result.items()

        # return num_epochs, bounds, qgan # TO UNCOMMENT
        return num_epochs, qgan, rel_entropy

        # ------------- TRAINING PROGRESS AND OUTCOME --------------

        # [moved to separate files]
