import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateCXNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateCXToAllNode"
    bl_label = "Quantum Gate CX To All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Controle Qubit", "controle_qubit", value = 0, minValue = 0)
        self.newInput("Integer", "Target Qubit", "target_qubit", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input ,controle_qubit ,target_qubit ):
        try:
            input.cx(controle_qubit,target_qubit)
            return input
        except:
            return