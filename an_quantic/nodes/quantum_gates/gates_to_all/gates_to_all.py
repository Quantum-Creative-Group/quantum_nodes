import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateSToAllNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateSToAllNode"
    bl_label = "Quantum Gate S To All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.s(j)
            return input
        except:
            return