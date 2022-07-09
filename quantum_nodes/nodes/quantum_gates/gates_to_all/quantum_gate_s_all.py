from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateSToAllNode(Node, AnimationNode):
    """Apply quantum gate S to all the circuit."""

    bl_idname = "an_QuantumGateSToAllNode"
    bl_label = "Quantum Gate S to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.s(j)
            return input
        except BaseException:
            return
