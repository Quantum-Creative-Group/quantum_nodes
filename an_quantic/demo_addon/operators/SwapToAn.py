import bpy, os, sys

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
                area.spaces[0].tree_type = 'an_AnimationNodeTree' 
                #if area.spaces[0].tree_type == 'an_AnimationNodeTree': print('YAHOUUUUUUUUUUUUUUUUUUUUUUUU')
        return {'FINISHED'}