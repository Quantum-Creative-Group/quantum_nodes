import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateTDGToAllNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateTDGToAllNode"
    bl_label = "Quantum Gate TDG To All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.tdg(j)
            return input
        except:
            return