from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateCCXNode(Node, AnimationNode):
    """Apply quantum gate CCX to the circuit."""

    bl_idname = "an_QuantumGateCCXNode"
    bl_label = "Quantum Gate CCX"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "First Control Qubit Index", "controle_qubit_1", value=0, minValue=0)
        self.newInput("Integer", "Second Control Qubit Index", "controle_qubit_2", value=1, minValue=0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value=2, minValue=0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, controle_qubit_1, controle_qubit_2, target_qubit):
        if input.num_qubits < 3:
            self.raiseErrorMessage("There has to be at least three qubits in the circuit to use this gate")
        elif controle_qubit_1 >= input.num_qubits:
            self.raiseErrorMessage("The first Control qubit index must be lower than " + str(input.num_qubits))
        elif controle_qubit_2 >= input.num_qubits:
            self.raiseErrorMessage("The second Control qubit index must be lower than " + str(input.num_qubits))
        elif target_qubit >= input.num_qubits:
            self.raiseErrorMessage("The target qubit index must be lower than " + str(input.num_qubits))
        elif controle_qubit_1 < 0:
            self.raiseErrorMessage("The first Control qubit index must be positive")
        elif controle_qubit_2 < 0:
            self.raiseErrorMessage("The second Control qubit index must be positive")
        elif target_qubit < 0:
            self.raiseErrorMessage("The target qubit index must be positive")
        elif controle_qubit_1 == controle_qubit_2:
            self.raiseErrorMessage("The two Control qubits must be different")
        elif controle_qubit_1 == target_qubit:
            self.raiseErrorMessage("The first Control qubit must be different from the target qubit")
        elif controle_qubit_2 == target_qubit:
            self.raiseErrorMessage("The second Control qubit must be different from the target qubit")
        else:
            input.ccx(controle_qubit_1, controle_qubit_2, target_qubit)
            return input
