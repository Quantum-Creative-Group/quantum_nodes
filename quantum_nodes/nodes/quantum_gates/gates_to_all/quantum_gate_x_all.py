import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateXToAllNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateXToAllNode"
    bl_label = "Quantum Gate X to All Circuit"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.x(j)
            return input
        except:
            return