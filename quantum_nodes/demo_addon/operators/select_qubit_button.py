import bpy
from bpy.types import Operator
from bpy.props import IntProperty


class SelectQubitButton(Operator):
    """Button to select a qubit."""

    bl_idname = "object.select_qubit_button"
    bl_label = "Select qubit button Operator"

    index: IntProperty(
        name="Index", # noqa F821
        description="Index of the qubit",
        default=0,
        soft_min=0,
        min=0
    )

    def execute(self, context):
        bpy.types.Object.select_index = self.index
        context.scene.frame_set(context.scene.frame_current)
        return {'FINISHED'}
