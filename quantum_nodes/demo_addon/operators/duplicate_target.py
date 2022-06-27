import bpy
from bpy.types import Operator


class DuplicateTarget(Operator):
    bl_idname = "object.duplicate_target"
    bl_label = "Duplicate Target"
    bl_description = "Creates a brand new copy of your work"

    @classmethod
    def poll(cls, context):
        if context.object is None:
            return False
        return (context.object.select_get()) and (bpy.context.active_object == bpy.types.Scene.demo_manager.target)

    def execute(self, context):
        dm = bpy.types.Scene.demo_manager
        if dm.ntm.main_node_tree is not None:
            obj = dm.ntm.main_node_tree.nodes[dm.ntm.main_tree_id + "data_interface" + "_main"].value
            obj_name = obj.name.split(".")[0] + "_copy_" + dm.ntm.demo_id[:len(dm.ntm.demo_id) - 1]

            mesh_data = obj.copy().to_mesh()
            mesh_data = bpy.data.meshes.new_from_object(obj)
            mesh_data.name = "Mesh_" + obj_name
            copy_obj = bpy.data.objects.new(obj_name, mesh_data)
            copy_obj.location[1] -= 5.0

            name_collection_target = dm.target.users_collection[0].name
            for collection in bpy.data.collections.values():
                if collection.name == name_collection_target:
                    collection.objects.link(copy_obj)
        return {'FINISHED'}
