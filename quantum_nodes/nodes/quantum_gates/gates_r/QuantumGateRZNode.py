import bpy
from qiskit import execute
from math import pi
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateRZNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateRZNode"
    bl_label = "Quantum Gate RZ"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Float", "Angle", "angle", value = pi)
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, angle, qubit_index):
        if qubit_index >= input.num_qubits:
            self.raiseErrorMessage("The qubit index must be lower than " + str(input.num_qubits))
        elif qubit_index <0:
            self.raiseErrorMessage("The qubit index must be positive")
        else:
            input.rz(angle,qubit_index)
            return input
            