import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

class SwapToAn(bpy.types.Operator):
    bl_idname = "screen.swap_to_an"
    bl_label = "Add Material"
    bl_description = "Add New Material"

    def execute(self,context):
        #bpy.ops.screen.space_type_set_or_cycle(space_type='NODE_EDITOR')
        start_areas = context.screen.areas[:]
        bpy.ops.screen.area_split(direction='HORIZONTAL', factor=0.5)
        for area in context.screen.areas:
            if area not in start_areas:
                area.type = 'NODE_EDITOR'


        #if bpy.types.Panel.bl_idname == 'AN_PT_tree_panel': print("coucou")            TESTER SI L'IDNAME CORRESPOND A ANIMATION NODE
        return {'FINISHED'}