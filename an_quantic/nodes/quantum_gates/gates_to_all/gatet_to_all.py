import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode

class QuantumGateTToAllNode(bpy.types.Node, AnimationNode):
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
        except:
            return