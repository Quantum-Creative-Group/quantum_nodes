import bpy
from bpy.types import Operator


class SelectObject(Operator):
    """Select a new target object."""

    bl_idname = "object.select_object"
    bl_label = "Set a new target"

    @classmethod
    def poll(cls, context):
        forbidden_names = [
            "QuantumBlochSphere",
            "QuantumBlochSphereParent",
            "QuantumHistogramParent",
            "QuantumCityParent"]
        if context.object is None:
            return False
        return (context.object.select_get()) and (context.active_object.type == 'MESH')\
            and ("Animation Nodes" not in context.active_object.users_collection[0].name)\
            and context.active_object.name not in forbidden_names
        # TODO: improve security on third condition
        # (blender crashes when the created object is selected as the new target)

    def execute(self, context):
        dm = context.scene.demo_manager
        if dm.target != context.active_object:
            if dm.target is not None:
                self.report({'INFO'}, "QN Demo: target successfully updated")
            dm.initializeDemoNodeTree()
            dm.setNewTarget(context.active_object)
            for node_group in bpy.data.node_groups:
                if dm.ntm.main_tree_id + "an_q" in node_group.name:
                    bpy.ops.an.execute_tree(name=dm.ntm.main_tree_id + "an_q")

        # forces to redraw the view (magic trick)
        # TODO: find a better solution for it
        context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}

    def invoke(self, context, event):
        dm = context.scene.demo_manager
        if context.active_object != dm.target and dm.target is not None and context.active_object.type == 'MESH':
            return context.window_manager.invoke_confirm(self, event)
        self.execute(context)   # not sure about that lol
        # TODO: there must be a better solution
        return {'FINISHED'}
