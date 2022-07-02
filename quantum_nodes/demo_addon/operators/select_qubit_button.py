import bpy
from bpy.types import Operator
from bpy.props import IntProperty


class SelectQubitButton(Operator):
    """Button to select a qubit."""

    bl_idname = "object.select_qubit_button"
    bl_label = "Select qubit button Operator"

    index: IntProperty(default=0)

    def execute(self, context):
        bpy.types.Object.select_index = self.index
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}
