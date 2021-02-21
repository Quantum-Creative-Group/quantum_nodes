import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateCYNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateCYNode"
    bl_label = "Quantum Gate CY"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Controle Qubit Index", "controle_qubit", value = 0, minValue = 0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value = 1, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, controle_qubit, target_qubit):
        if input.num_qubits < 2:
            self.raiseErrorMessage("There has to be at least two qubits in the circuit to use this gate")
        if target_qubit >= input.num_qubits:
            self.raiseErrorMessage("The target qubit index must be lower than " + str(input.num_qubits))
        if controle_qubit == target_qubit:
            self.raiseErrorMessage("The controle qubit must be different from the target qubit")
        else:
            input.cy(controle_qubit, target_qubit)
            return input