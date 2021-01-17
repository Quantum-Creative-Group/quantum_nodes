import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateXToAllNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateXToAllNode"
    bl_label = "Quantum GateX To All Circuit"

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