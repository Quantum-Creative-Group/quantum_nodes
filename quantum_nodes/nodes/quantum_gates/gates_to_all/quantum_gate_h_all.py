from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateHToAllNode(Node, AnimationNode):
    """Apply quantum gate H to all the circuit."""

    bl_idname = "an_QuantumGateHToAllNode"
    bl_label = "Quantum Gate H to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.h(j)
            return input
        except BaseException:
            return
