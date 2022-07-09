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
from bpy.types import Node

import numpy as np
from qiskit.utils import algorithm_globals
from animation_nodes.base_types import AnimationNode
# from qiskit_finance.circuit.library import UniformDistribution # does not seem to be needed
# from qiskit_machine_learning.algorithms import NumPyDiscriminator, QGAN # needed?

from ... visualization.utils.qgan_edit_histogram import editQganHistogram

seed = 71
np.random.seed = seed
algorithm_globals.random_seed = seed


# Goal: Plot the CDF of the resulting distribution against the target distribution, i.e. log-normal
class QganHistogramNode(Node, AnimationNode):
    """Generate a new histogram."""

    bl_idname = "an_QganHistogramNode"
    bl_label = "qGAN Histogram"

    def create(self):
        # self.newInput("Integer", "Shots", "shots", value = 1024, minValue = 1)
        # self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        # self.newInput("Array", "Bounds", "bounds") # TO UNCOMMENT ASAP
        self.newInput("Object", "qGAN Histogram", "qganHistogram")
        # self.newInput("Object", "Histogram", "histogram")
        self.newInput("QGAN", "qGAN", "qgan")

    def execute(self, qganHistogram, qgan):
        # if qganHistogram is None or qgan is None:
        if qganHistogram is None:
            return
        if qganHistogram.name != "QuantumQganHistogramFaces":
            return
        try:
            # quantum_circuit.measure_all()
            # backend = Aer.get_backend('qasm_simulator')
            # job = execute(quantum_circuit, backend, shots = shots)
            # counts = job.result().get_counts(quantum_circuit)

            bounds = np.array([0.0, 3.0])  # TODO: DUPLICATE DECLARATION FROM qgan_run.py, THIS MUST BE REMOVED ASAP

            # -------- For rectangular parallelepipeds of Target, i.e. Training Data ----------
            # list of 100000 values (training data) ; 100000 took too long
            log_normal = np.random.lognormal(mean=1, sigma=1, size=100000)
            log_normal = np.round(log_normal)  # round to closest integer values
            log_normal = log_normal[log_normal <= bounds[1]]  # get rid of values exceeding bounds[1], i.e. 3.0
            temp = []
            for i in range(int(bounds[1] + 1)):
                # temp is the list of summed occurrences for each value (ascendant) in log_normal
                temp += [np.sum(log_normal == i)]
            log_normal = np.array(temp / sum(temp))  # log_normal becomes a normalized version of temp
            cum_log_normal = np.cumsum(log_normal)
            # dict of indices associated with their "probability"
            targetCounts = {}
            for i in range(len(cum_log_normal)):
                # str(i) corresponds to the sample values of cum_log_normal because the
                # latter are rounded to integers for better graph visualization
                targetCounts[str(i)] = cum_log_normal[i]
            # ----------------------------------------------------------------------------------

            # -------- For rectangular parallelepipeds of Simulation, i.e. Output of qGAN's Generator ----------
            # Extract samples' values as an array
            samples_g, prob_g = qgan.generator.get_output(qgan.quantum_instance, shots=10000)  # 10000 took too long
            samples_g = np.array(samples_g)
            samples_g = samples_g.flatten()
            cum_prob_g = np.cumsum(prob_g)
            simulationCounts = {}
            for i in range(len(cum_prob_g)):
                simulationCounts[str(samples_g[i])] = cum_prob_g[i]
            # ----------------------------------------------------------------------------------

            # shots =

            # What do these instructions do?
            parent = qganHistogram.parent
            for i in range(len(qganHistogram.children)):
                bpy.data.objects.remove(qganHistogram.children[0])
            bpy.data.objects.remove(qganHistogram)

            # TODO : reimplement the "shots" as a variable into the function process,
            # now for both the training data and the generator samples
            editQganHistogram(parent, targetCounts, simulationCounts)
        except BaseException:
            return
