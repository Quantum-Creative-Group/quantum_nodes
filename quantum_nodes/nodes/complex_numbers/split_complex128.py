from bpy.types import Node
from animation_nodes.base_types import AnimationNode


class SplitComplex128Node(Node, AnimationNode):
    """Implementation of the numpy double complex data type."""

    bl_idname = "an_SplitComplex128"
    bl_label = "Split complex128"

    def create(self):
        self.newInput("Complex128", "Complex128", "complex128")
        self.newOutput("Float", "Real part", "real_part")
        self.newOutput("Float", "Imaginary part", "imaginary_part")

    def execute(self, complex128):
        return (complex128.real, complex128.imag)
