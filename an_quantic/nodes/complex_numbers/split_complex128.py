import bpy
from numpy import complex128
from animation_nodes.base_types import AnimationNode

class SplitComplex128Node(bpy.types.Node, AnimationNode):
    bl_idname = "an_SplitComplex128"
    bl_label = "Split complex128"

    
    def create(self):
        self.newInput("Complex128", "Complex128", "complex128")

        self.newOutput("Float", "Real part", "real_part")
        self.newOutput("Float", "Imaginary part", "imaginary_part")

    def execute(self, complex128):
        return (complex128.real, complex128.imag)