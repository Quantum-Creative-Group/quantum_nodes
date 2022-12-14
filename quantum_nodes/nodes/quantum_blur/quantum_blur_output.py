from bpy.types import Node

from math import ceil, sqrt
from animation_nodes.base_types import AnimationNode
from animation_nodes.data_structures import DoubleList

from ... lib.quantumblur import circuit2height


class QuantumBlurOutputNode(Node, AnimationNode):
    """Output of the Quantum Blur algorithm."""

    bl_idname = "an_QuantumBlurOutputNode"
    bl_label = "Quantum Blur Output"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "qc")
        self.newOutput("Float List", "Floats", "floats")

    def execute(self, qc):
        try:
            floats = DoubleList()
            dictFloats = {}
            dictFloats = circuit2height(qc)
            n = int(ceil(sqrt(len(dictFloats))))
            for i in range(n):
                for j in range(n):
                    floats.append(dictFloats[i, j])
            return floats
        except BaseException:
            return
