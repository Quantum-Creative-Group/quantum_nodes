from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateSDGToAllNode(Node, AnimationNode):
    """Apply quantum gate SDG to all the circuit."""

    bl_idname = "an_QuantumGateSDGToAllNode"
    bl_label = "Quantum Gate SDG to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.sdg(j)
            return input
        except BaseException:
            return
