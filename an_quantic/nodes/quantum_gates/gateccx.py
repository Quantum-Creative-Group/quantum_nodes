import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateCCXNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateCCXNode"
    bl_label = "Quantum Gate CCX"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "First Controle Qubit Index", "controle_qubit_1", value = 0, minValue = 0)
        self.newInput("Integer", "Second Controle Qubit Index", "controle_qubit_2", value = 1, minValue = 0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value = 3, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input ,controle_qubit_1,controle_qubit_2 ,target_qubit ):
        try:
            input.ccx(controle_qubit_1, controle_qubit_2,target_qubit)
            return input
        except:
            return