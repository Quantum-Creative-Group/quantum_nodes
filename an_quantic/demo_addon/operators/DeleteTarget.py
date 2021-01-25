import bpy
from bpy.types import Operator

class DeleteTarget(Operator):
    bl_idname = "object.delete_target"
    bl_label = "Delete Target"
    bl_description = "Deletes the current target"

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and bpy.context.active_object == bpy.types.Scene.demo_manager.target
    
    def execute(self, context):
        self.report({'INFO'}, "AN_Q_DEMO : target successfully removed")
        bpy.types.Scene.demo_manager.removeAll()
        return{'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)