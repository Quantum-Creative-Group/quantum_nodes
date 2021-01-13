import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumNode"
    bl_label = "Quantum Node"

    def create(self):
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("QuantumCircuit", "QuantumCircuit", "quantumCircuit")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return

        target.location = source.location + offset