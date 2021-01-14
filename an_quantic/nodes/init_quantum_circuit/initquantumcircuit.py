import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class InitQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_InitQuantumCircuitNode"
    bl_label = "Init Quantum Circuit"

    def create(self):
        self.newInput("Integer", "Number Of Qubits", "number_of_qubits")
        self.newOutput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")

    def execute(self, number_of_qubits):
        try:
            return QuantumCircuit(number_of_qubits)
        except:
            return