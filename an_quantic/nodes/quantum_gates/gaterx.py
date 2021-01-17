import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateRXNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateRXNode"
    bl_label = "Quantum Gate RX Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Float", "Angle", "angle")
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input ,controle_qubit ,target_qubit ):
        try:
            input.rx(angle,qubit_index)
            return input
        except:
            return