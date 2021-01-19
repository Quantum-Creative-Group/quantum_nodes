import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumNode"
    bl_label = "Quantum Node"

    def create(self):
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("Quantum Register", "Quantum Register", "quantumregister")

    def execute(self):
        if source is None or target is None:
            return
