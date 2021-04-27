import bpy
import bmesh
import mathutils
import math
import numpy as np
from qiskit import *
import math
from animation_nodes.base_types import AnimationNode
from ... visualization.utils.editHistogram import editHistogram

class EditHistogrameNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_EditHistogrameNode"
    bl_label = "Edit Histograme"

    def create(self):
        self.newInput("Integer", "Shots", "shots", value = 1024, minValue = 1)
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Object", "Histograme", "histograme")

    def execute(self, shots, quantum_circuit, histograme):
        if histograme is None:
            return
        if (histograme.name != "QuantumHistogrameFaces") :
            return 
        try:
            quantum_circuit.measure_all()
            backend = Aer.get_backend('qasm_simulator')
            job = execute(quantum_circuit, backend, shots = shots)
            counts = job.result().get_counts(quantum_circuit)

            parent = histograme.parent
            for i in range (len(histograme.children)):
                bpy.data.objects.remove(histograme.children[0])
            bpy.data.objects.remove(histograme)
            editHistogram(parent, counts, shots)       
        except:
            return