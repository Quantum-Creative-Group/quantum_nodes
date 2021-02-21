import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateCCXNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateCCXNode"
    bl_label = "Quantum Gate CCX"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "First Controle Qubit Index", "controle_qubit_1", value = 0, minValue = 0)
        self.newInput("Integer", "Second Controle Qubit Index", "controle_qubit_2", value = 1, minValue = 0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value = 2, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, controle_qubit_1, controle_qubit_2, target_qubit):
        if input.num_qubits < 3:
            self.raiseErrorMessage("There has to be at least three qubits in the circuit to use this gate")
        elif controle_qubit_1 >= input.num_qubits:
            self.raiseErrorMessage("The first controle qubit index must be lower than " + str(input.num_qubits))
        elif controle_qubit_2 >= input.num_qubits:
            self.raiseErrorMessage("The second controle qubit index must be lower than " + str(input.num_qubits))
        elif target_qubit >= input.num_qubits:
            self.raiseErrorMessage("The target qubit index must be lower than " + str(input.num_qubits))
        elif controle_qubit_1 == controle_qubit_2:
            self.raiseErrorMessage("The two controle qubits must be different")
        elif controle_qubit_1 == target_qubit:
            self.raiseErrorMessage("The first controle qubit must be different from the target qubit")
        elif controle_qubit_2 == target_qubit:
            self.raiseErrorMessage("The second controle qubit must be different from the target qubit")
        else:
            input.ccx(controle_qubit_1, controle_qubit_2,target_qubit)
            return input