import bpy
from bpy.types import Operator

class SwitchToAn(Operator):
    bl_idname = "screen.switch_to_an"
    bl_label = "Redirects the user to the animation nodes editor"
    bl_description = "Behind the scenes"

    def execute(self,context):
        start_areas = context.screen.areas[:]
        bpy.ops.screen.area_split(direction='HORIZONTAL', factor=0.5)
        for area in context.screen.areas:
            if area not in start_areas:
                area.type = 'NODE_EDITOR'
                area.spaces[0].tree_type = 'an_AnimationNodeTree' 
        return {'FINISHED'}
