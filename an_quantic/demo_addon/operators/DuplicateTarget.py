import bpy
from bpy.types import Operator

class DuplicateTarget(Operator):
    bl_idname = "object.duplicate_target"
    bl_label = "Duplicate Target"
    bl_description = "Creates a brand new copy of your work"
    
    def execute(self, context):
        print("lol")
        return{'FINISHED'}