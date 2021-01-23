import bpy, os, sys

class SelectQubitButton(bpy.types.Operator):
    bl_idname = "object.select_qubit_button"
    bl_label = "Select qubit button Operator"
    
    index: bpy.props.IntProperty(default = 0)

    def execute(self, context):
        bpy.types.Object.select_index = self.index
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return{'FINISHED'}