import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateCZNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateCZToAllNode"
    bl_label = "Quantum Gate CZ To All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Controle Qubit Index", "controle_qubit", value = 0, minValue = 0)
        self.newInput("Integer", "Target Qubit Index", "target_qubit", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input ,controle_qubit ,target_qubit ):
        try:
            input.cz(controle_qubit,target_qubit)
            return input
        except:
            return