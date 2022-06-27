from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node


class QuantumGateCZNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateCZNode"
    bl_label = "Quantum Gate CZ"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Control Qubit Index", "controle_qubit", value=0, minValue=0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value=1, minValue=0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, controle_qubit, target_qubit):
        if input.num_qubits < 2:
            self.raiseErrorMessage("There has to be at least two qubits in the circuit to use this gate")
        elif controle_qubit >= input.num_qubits:
            self.raiseErrorMessage("The Control qubit index must be lower than " + str(input.num_qubits))
        elif target_qubit >= input.num_qubits:
            self.raiseErrorMessage("The target qubit index must be lower than " + str(input.num_qubits))
        elif controle_qubit == target_qubit:
            self.raiseErrorMessage("The Control qubit must be different from the target qubit")
        elif controle_qubit < 0:
            self.raiseErrorMessage("The Control qubit index must be positive")
        elif target_qubit < 0:
            self.raiseErrorMessage("The target qubit index must be positive")
        else:
            input.cz(controle_qubit, target_qubit)
            return input
