import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateCYNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateCYNode"
    bl_label = "Quantum Gate CY"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Controle Qubit Index", "controle_qubit", value = 0, minValue = 0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, controle_qubit, target_qubit):
        if (target_qubit >= input.num_qubits) :
            self.raiseErrorMessage("The target qubit index must lower than " + str(input.num_qubits))
        if (controle_qubit >= input.num_qubits) :
            self.raiseErrorMessage("The controle qubit index must lower than " + str(input.num_qubits))
        if (controle_qubit==target_qubit) :
            self.raiseErrorMessage("The controle qubit must be different from the target qubit")
        try:
            input.cy(controle_qubit, target_qubit)
            return input
        except:
            return