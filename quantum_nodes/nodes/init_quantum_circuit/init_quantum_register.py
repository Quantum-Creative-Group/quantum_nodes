from qiskit import QuantumRegister
from animation_nodes.base_types import AnimationNode
from bpy.types import Node


class InitQuantumRegisterNode(Node, AnimationNode):
    """Create and initialize a quantum register."""

    bl_idname = "an_InitQuantumRegisterNode"
    bl_label = "Init Quantum Register"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Integer", "Number Of Qubits", "number_of_qubits", value=1, minValue=1)
        self.newOutput("Quantum Register", "Quantum Register", "quantum_register")

    def execute(self, number_of_qubits):
        if(number_of_qubits < 1):
            self.raiseErrorMessage("The number of qubits must be superior to 1")
            return
        else:
            return QuantumRegister(number_of_qubits)
