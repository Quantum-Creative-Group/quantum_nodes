import bpy, os, sys
from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager

class SelectObject(bpy.types.Operator):
    bl_idname = "object.select_object"
    bl_label = "Ok = Delete the current circuit"

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        self.report({'INFO'}, "Object has changed")
        DEMO_Manager.selected_obj = bpy.context.active_object
        return {'FINISHED'}

    def invoke(self, context, event):   
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if context.active_object != DEMO_Manager.selected_obj and context.active_object.type == 'MESH': 
            return context.window_manager.invoke_confirm(self, event)
        return {'FINISHED'}
