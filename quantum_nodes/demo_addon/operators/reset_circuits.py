import bpy
from bpy.types import Operator


class ResetCircuits(Operator):
    """Reset all circuits."""

    bl_idname = "object.reset_quantum_circuits"
    bl_label = "Reset circuits"
    bl_description = "Resets every quantum circuit"

    @classmethod
    def poll(cls, context):
        if context.object is None:
            return False
        return (context.object.select_get()) and (bpy.context.active_object == bpy.types.Scene.demo_manager.target)

    def execute(self, context):
        self.report({'INFO'}, "QN Demo: quantum circuits successfully reset")
        dm = bpy.types.Scene.demo_manager
        dm.resetCircuits()
        dm.setNewCircuits(dm.target)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
