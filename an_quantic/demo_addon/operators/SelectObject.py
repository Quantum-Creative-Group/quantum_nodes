import bpy, os, sys
from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager

class SelectObject(bpy.types.Operator):
    bl_idname = "object.select_object"
    bl_label = "Ok = Delete the current circuit"

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        #if context.active_object != DEMO_Manager.selected_obj:
        #self.layout.label('hello')
        print(self)
        self.report({'INFO'}, "coucou")
        DEMO_Manager.selected_obj = bpy.context.active_object
        
        return {'FINISHED'}

    def invoke(self, context, event):   
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if context.active_object != DEMO_Manager.selected_obj: 
            return context.window_manager.invoke_confirm(self, event)
        return {'FINISHED'}
