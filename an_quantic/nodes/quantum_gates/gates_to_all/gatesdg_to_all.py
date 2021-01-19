import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateSDGToAllNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateSDGToAllNode"
    bl_label = "Quantum Gate SDG To All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.sdg(j)
            return input
        except:
            return