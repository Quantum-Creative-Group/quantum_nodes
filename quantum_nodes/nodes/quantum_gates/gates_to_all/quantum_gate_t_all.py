from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateTToAllNode(Node, AnimationNode):
    """Apply quantum gate T to all the circuit."""

    bl_idname = "an_QuantumGateTToAllNode"
    bl_label = "Quantum Gate T to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.t(j)
            return input
        except BaseException:
            return
