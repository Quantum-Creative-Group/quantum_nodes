import bpy
from bpy.types import Operator
from bpy.props import IntProperty

class CreateNewMesh(Operator):
    bl_idname = "mesh.create_mesh"
    bl_label = "Create a mesh"
    bl_description = "Creates a new mesh"

    subs: IntProperty(name="subs", default=2, min=1, max=100)

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        obj = bpy.context.active_object
        obj.modifiers.new("an_q_demo_subdivide_op", 'SUBSURF')
        return {'FINISHED'}
