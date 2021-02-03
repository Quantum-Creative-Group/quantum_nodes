import bpy
from qiskit import QuantumRegister
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class InitQuantumRegisterNode(Node, AnimationNode):
    bl_idname = "an_InitQuantumRegisterNode"
    bl_label = "Init Quantum Register"

    def create(self):
        self.newInput("Integer", "Number Of Qubits", "number_of_qubits", value = 1, minValue = 1)
        self.newOutput("Quantum Register", "Quantum Register", "quantum_register")

    def execute(self, number_of_qubits):
        try:
            return QuantumRegister(number_of_qubits)
        except:
            return