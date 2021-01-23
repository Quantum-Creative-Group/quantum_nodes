import bpy, os, sys
from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager

class SelectObject(bpy.types.Operator):
    """Setting a new target will erase the current circuits"""

    bl_idname = "object.select_object"
    bl_label = "Set a new target"

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        self.report({'INFO'}, "AN_Q_DEMO : target successfully updated")
        DEMO_Manager.reset()
        DEMO_Manager.createNewCircuit(bpy.context.active_object)
        
        # forces to redraw the view (magic trick)
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}

    def invoke(self, context, event):   
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if context.active_object != DEMO_Manager.selected_obj and context.active_object.type == 'MESH': 
            return context.window_manager.invoke_confirm(self, event)
        return {'FINISHED'}
