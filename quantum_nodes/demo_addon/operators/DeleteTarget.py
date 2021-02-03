import bpy
from bpy.types import Operator

class DeleteTarget(Operator):
    bl_idname = "object.delete_target"
    bl_label = "Delete Target"
    bl_description = "Deletes the current target"
    
    def execute(self, context):
        self.report({'INFO'}, "AN_Q_DEMO: target successfully removed")
        if bpy.types.Scene.demo_manager.target != None:
            bpy.types.Scene.demo_manager.removeAll()
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)