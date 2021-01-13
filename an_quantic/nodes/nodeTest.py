import bpy
from animation_nodes.base_types import AnimationNode
from an_quantic.sockets.test_socket import QuantumSocket

class CopyLocationWithOffsetNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_CopyLocationWithOffsetNode"
    bl_label = "Copy Location with Offset"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Quantum", "Offset", "offset")

    def execute(self, source, target, offset):
        if source is None or target is None:
            return

        target.location = source.location + offset