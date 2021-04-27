import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateCSWAPNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateCSWAPNode"
    bl_label = "Quantum Gate CSWAP"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "First Qubit Index", "first_qubit", value = 0, minValue = 0)
        self.newInput("Integer", "Second  Qubit Index", "second_qubit", value = 1, minValue = 0)
        self.newInput("Integer", "Control Qubit Index", "control_qubit", value = 2, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, first_qubit, second_qubit, control_qubit):
        if input.num_qubits < 3:
            self.raiseErrorMessage("There has to be at least three qubits in the circuit to use this gate")
        elif first_qubit >= input.num_qubits:
            self.raiseErrorMessage("The first qubit index must be lower than " + str(input.num_qubits))
        elif second_qubit >= input.num_qubits:
            self.raiseErrorMessage("The second qubit index must be lower than " + str(input.num_qubits))
        elif control_qubit >= input.num_qubits:
            self.raiseErrorMessage("The control qubit index must be lower than " + str(input.num_qubits))
        elif first_qubit < 0:
            self.raiseErrorMessage("The first qubit index must be positive")
        elif second_qubit < 0:
            self.raiseErrorMessage("The second qubit index must be positive")
        elif control_qubit < 0:
            self.raiseErrorMessage("The control qubit index must be positive")
        elif first_qubit == second_qubit:
            self.raiseErrorMessage("The two qubits must be different")
        elif first_qubit == control_qubit:
            self.raiseErrorMessage("The first qubit must be different from the control qubit")
        elif second_qubit == control_qubit:
            self.raiseErrorMessage("The second qubit must be different from the control qubit")
        else:
            input.cswap(control_qubit, first_qubit, second_qubit)
            return input