import bpy
from qiskit import ClassicalRegister
from animation_nodes.base_types import AnimationNode

class InitClassicalRegisterNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_InitClassicalRegisterNode"
    bl_label = "Init Classical Register"

    def create(self):
        self.newInput("Integer", "Number Of Bits", "number_of_bits", value = 1, minValue = 1)
        self.newOutput("Classical Register", "Classical Register", "classical_register")

    def execute(self, number_of_bits):
        try:
            return ClassicalRegister(number_of_bits)
        except:
            return