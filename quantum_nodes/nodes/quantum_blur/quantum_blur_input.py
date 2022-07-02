from bpy.types import Node
from ... lib.quantumblur import height2circuit
from animation_nodes.base_types import AnimationNode
from math import ceil, sqrt


class QuantumBlurInputNode(Node, AnimationNode):
    """Input of the Quantum Blur algorithm."""

    bl_idname = "an_QuantumBlurInputNode"
    bl_label = "Quantum Blur Input"

    def create(self):
        self.newInput("Float List", "Floats", "floats")
        self.newOutput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")

    def execute(self, floats):
        if floats == []:
            return 0
        dictFloats = {}
        n = int(ceil(sqrt(len(floats))))
        iterator = 0
        for i in range(n):
            for j in range(n):
                if iterator < len(floats):
                    dictFloats[i, j] = float(format(abs(floats[iterator]), '.3f'))
                else:
                    dictFloats[i, j] = 0.0
                iterator += 1
        circuit = height2circuit(dictFloats)
        return circuit
