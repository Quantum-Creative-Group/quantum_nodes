import bpy
from bpy.types import Node
from qiskit import *
from animation_nodes.base_types import AnimationNode
from ... visualization.utils.edit_histogram import editHistogram

class HistogramNode(Node, AnimationNode):
    bl_idname = "an_HistogramNode"
    bl_label = "Histogram"

    def create(self):
        self.newInput("Integer", "Shots", "shots", value = 1024, minValue = 1)
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Object", "Histogram", "histogram")

    def execute(self, shots, quantum_circuit, histogram):
        if histogram is None:
            return
        if (histogram.name != "QuantumHistogramFaces"):
            return 
        try:
            quantum_circuit.measure_all()
            backend = Aer.get_backend('qasm_simulator')
            job = execute(quantum_circuit, backend, shots = shots)
            counts = job.result().get_counts(quantum_circuit)

            parent = histogram.parent
            for i in range (len(histogram.children)):
                bpy.data.objects.remove(histogram.children[0])
            #bpy.data.objects.remove(histogram)
            editHistogram(parent, counts, shots)
        except:
            return