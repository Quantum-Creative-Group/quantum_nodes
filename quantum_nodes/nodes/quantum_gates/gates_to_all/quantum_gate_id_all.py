from bpy.types import Node

from animation_nodes.base_types import AnimationNode


class QuantumGateIDToAllNode(Node, AnimationNode):
    """Apply quantum gate ID to all the circuit."""

    bl_idname = "an_QuantumGateIDToAllNode"
    bl_label = "Quantum Gate ID to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.id(j)
            return input
        except BaseException:
            return
