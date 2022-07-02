from qiskit import ClassicalRegister
from animation_nodes.base_types import AnimationNode
from bpy.types import Node


class InitClassicalRegisterNode(Node, AnimationNode):
    """Create and initialize a classical register."""

    bl_idname = "an_InitClassicalRegisterNode"
    bl_label = "Init Classical Register"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Integer", "Number Of Bits", "number_of_bits", value=1, minValue=1)
        self.newOutput("Classical Register", "Classical Register", "classical_register")

    def execute(self, number_of_bits):
        if number_of_bits < 1:
            self.raiseErrorMessage("The number of bits must be superior to 1")
            return
        else:
            return ClassicalRegister(number_of_bits)
