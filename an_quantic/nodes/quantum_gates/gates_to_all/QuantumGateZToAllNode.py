import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateZToAllNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateZToAllNode"
    bl_label = "Quantum Gate Z to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.z(j)
            return input
        except:
            return