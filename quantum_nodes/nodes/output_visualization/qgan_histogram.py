import numpy as np
import bpy
from bpy.types import Node
from qiskit.pulse.builder import measure_all
from qiskit import (Aer, execute)
from animation_nodes.base_types import AnimationNode
from ... visualization.utils.qgan_edit_histogram import editQganHistogram

seed = 71
np.random.seed = seed

from qiskit import QuantumRegister, QuantumCircuit, BasicAer
from qiskit.circuit.library import TwoLocal
from qiskit_finance.circuit.library import UniformDistribution # does not seem to be needed
from qiskit.utils import QuantumInstance, algorithm_globals
from qiskit_machine_learning.algorithms import NumPyDiscriminator, QGAN # needed?

algorithm_globals.random_seed = seed

# Goal: Plot the CDF of the resulting distribution against the target distribution, i.e. log-normal

class QganHistogramNode(Node, AnimationNode):
    bl_idname = "an_QganHistogramNode"
    bl_label = "qGAN Histogram"

    def create(self):
        #self.newInput("Integer", "Shots", "shots", value = 1024, minValue = 1)
        #self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        #self.newInput("Array", "Bounds", "bounds") # TO UNCOMMENT ASAP
        self.newInput("Object", "qGAN Histogram", "qganHistogram")
        #self.newInput("Object", "Histogram", "histogram")
        self.newInput("QGAN", "qGAN", "qgan")

    def execute(self, qganHistogram, qgan):
        #if qganHistogram is None or qgan is None:
        if qganHistogram is None:
            return
        if (qganHistogram.name != "QuantumQganHistogramFaces"):
            return 
        try:
            #quantum_circuit.measure_all()
            #backend = Aer.get_backend('qasm_simulator')
            #job = execute(quantum_circuit, backend, shots = shots)
            #counts = job.result().get_counts(quantum_circuit)

            bounds = np.array([0.0, 3.0]) # TODO: DUPLICATE DECLARATION FROM qgan_run.py, THIS MUST BE REMOVED ASAP

            #-------- For rectangular parallelepipeds of Target, i.e. Training Data ----------
            log_normal = np.random.lognormal(mean=1, sigma=1, size=100000) # list of 100000 values (training data) ; 100000 took too long
            log_normal = np.round(log_normal) # round to closest integer values
            log_normal = log_normal[log_normal <= bounds[1]] # get rid of values exceeding bounds[1], i.e. 3.0
            temp = []
            for i in range(int(bounds[1] + 1)):
                temp += [np.sum(log_normal == i)] # temp is the list of summed occurrences for each value (ascendant) in log_normal
            log_normal = np.array(temp / sum(temp)) # log_normal becomes a normalized version of temp
            cum_log_normal = np.cumsum(log_normal)
            # dict of indices associated with their "probability"
            targetCounts = {}
            for i in range(len(cum_log_normal)) :
                targetCounts[str(i)] = cum_log_normal[i] # str(i) corresponds to the sample values of cum_log_normal because the latter are rounded to integers for better graph visualization
            #----------------------------------------------------------------------------------

            #-------- For rectangular parallelepipeds of Simulation, i.e. Output of qGAN's Generator ----------
            # Extract samples' values as an array
            samples_g, prob_g = qgan.generator.get_output(qgan.quantum_instance, shots=10000) # 10000 took too long
            samples_g = np.array(samples_g)
            samples_g = samples_g.flatten()
            cum_prob_g = np.cumsum(prob_g)
            #num_bins = len(prob_g) # seems useless
            #plt.xticks(np.arange(min(samples_g), max(samples_g) + 1, 1.0)) # TO BE REMOVED (was for matplotlib graph)
            simulationCounts = {}
            for i in range(len(cum_prob_g)) :
                simulationCounts[str(samples_g[i])] = cum_prob_g[i]
            #----------------------------------------------------------------------------------

            #shots = 

            # What do these instructions do?
            parent = qganHistogram.parent
            for i in range (len(qganHistogram.children)):
                bpy.data.objects.remove(qganHistogram.children[0])
            bpy.data.objects.remove(qganHistogram)

            editQganHistogram(parent, targetCounts, simulationCounts) #TODO : reimplement the "shots" as a variable into the function process, now for both the training data and the generator samples
        except:
            return