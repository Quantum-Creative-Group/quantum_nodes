import bpy
from bpy.types import Operator

class SelectObject(Operator):
    """Setting a new target will erase the current circuits"""

    bl_idname = "object.select_object"
    bl_label = "Set a new target"

    def execute(self, context):
        dm = bpy.types.Scene.QuantumNodes_DEMO_Manager
        self.report({'INFO'}, "AN_Q_DEMO : target successfully updated")
        dm.reset()
        dm.createNewCircuit(bpy.context.active_object)
        
        # forces to redraw the view (magic trick)
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}

    def invoke(self, context, event):   
        dm = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if context.active_object != dm.selected_obj and context.active_object.type == 'MESH': 
            return context.window_manager.invoke_confirm(self, event)
        return {'FINISHED'}
