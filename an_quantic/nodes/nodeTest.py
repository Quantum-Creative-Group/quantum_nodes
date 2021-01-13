import bpy
from animation_nodes.base_types import AnimationNode

class QuantumNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumNode"
    bl_label = "Quantum Node"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("QuantumCircuit", "Offset", "offset")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return

        target.location = source.location + offset