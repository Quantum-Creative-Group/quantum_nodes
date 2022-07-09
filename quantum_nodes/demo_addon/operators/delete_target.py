from bpy.types import Operator


class DeleteTarget(Operator):
    """Delete the current target (selected object)."""

    bl_idname = "object.delete_target"
    bl_label = "Delete Target"
    bl_description = "Deletes the current target"

    def execute(self, context):
        self.report({'INFO'}, "QN Demo: target successfully removed")
        if context.scene.demo_manager.target is not None:
            context.scene.demo_manager.removeAll()
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
