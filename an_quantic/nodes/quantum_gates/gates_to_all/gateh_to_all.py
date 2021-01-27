import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode

class QuantumGateHToAllNode(bpy.types.Node, AnimationNode):
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
        except:
            return