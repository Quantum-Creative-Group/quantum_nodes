import bpy
from bpy.types import Operator

class SelectObject(Operator):
    """Setting a new target will erase the current circuits"""

    bl_idname = "object.select_object"
    bl_label = "Set a new target"

    @classmethod
    def poll(cls, context):
        if context.object == None: return False
        return (context.object.select_get()) and (context.active_object.type == 'MESH')\
            and ("Animation Nodes" not in context.active_object.users_collection[0].name)
            # TODO: improve security on third condition 
            # (blender crashes when the created object is selected as the new target)

    def execute(self, context):
        dm = bpy.types.Scene.demo_manager
        if dm.target != bpy.context.active_object:
            if dm.target != None:
                self.report({'INFO'}, "AN_Q_DEMO : target successfully updated")
            dm.initializeDemoNodeTree()
            dm.setNewTarget(bpy.context.active_object)
            bpy.ops.an.execute_tree(name=dm.ntm.main_tree_id+"an_q")
        
        # forces to redraw the view (magic trick)
        # TODO: find a better solution for it
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}

    def invoke(self, context, event):
        dm = bpy.types.Scene.demo_manager
        if (context.active_object != dm.target) and (dm.target != None) and (context.active_object.type == 'MESH'):
            return context.window_manager.invoke_confirm(self, event)
        self.execute(context) # not sure about that lol
        # TODO: there must be a better solution
        return {'FINISHED'}
