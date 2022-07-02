from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node


class QuantumGateSWAPNode(Node, AnimationNode):
    """Apply quantum gate SWAP to selected qubits."""

    bl_idname = "an_QuantumGateSWAPNode"
    bl_label = "Quantum Gate SWAP"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "First Qubit Index", "first_qubit", value=0, minValue=0)
        self.newInput("Integer", "Second Qubit Index", "second_qubit", value=1, minValue=0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, first_qubit, second_qubit):
        if input.num_qubits < 2:
            self.raiseErrorMessage("There has to be at least two qubits in the circuit to use this gate")
        elif first_qubit >= input.num_qubits:
            self.raiseErrorMessage("The first qubit index must be lower than " + str(input.num_qubits))
        elif second_qubit >= input.num_qubits:
            self.raiseErrorMessage("The second qubit index must be lower than " + str(input.num_qubits))
        elif first_qubit < 0:
            self.raiseErrorMessage("The first qubit index must be positive")
        elif second_qubit < 0:
            self.raiseErrorMessage("The second qubit index must be positive")
        elif first_qubit == second_qubit:
            self.raiseErrorMessage("The first qubit must be different from the second one")
        else:
            input.swap(first_qubit, second_qubit)
            return input
