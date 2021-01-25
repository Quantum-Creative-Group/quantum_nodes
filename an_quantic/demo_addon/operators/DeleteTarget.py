import bpy
from bpy.types import Operator

class DeleteTarget(Operator):
    bl_idname = "object.delete_target"
    bl_label = "Delete Target"
    bl_description = "Deletes the actual target"
    
    def execute(self, context):
        print("ptdr")
        return{'FINISHED'}