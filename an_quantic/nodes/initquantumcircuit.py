import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class InitQuantumCircuit(bpy.types.Node, AnimationNode):
    bl_idname = "an_InitQuantumCircuit"
    bl_label = "Init Quantum Circuit"

    def create(self):
        self.newInput("Integer", "Number Of Qubits", "number_of_qubits")
        self.newOutput("QuantumCircuit", "QuantumCircuit", "quantum_circuit")

    def execute(self, number_of_qubits):
        try:
            return QuantumCircuit(number_of_qubits)
        except:
            return