import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateYToAllNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateYToAllNode"
    bl_label = "Quantum Gate Y to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.y(j)
            return input
        except:
            return