import bpy
from bpy.props import IntProperty

class CreateNewMesh(bpy.types.Operator):
    bl_idname = "mesh.create_mesh"
    bl_label = "Create a mesh"
    bl_description = "Creates a new mesh"

    subs: bpy.props.IntProperty(name="subs", default=2, min=1, max=100)

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        obj = bpy.context.active_object
        obj.modifiers.new("an_q_demo_subdivide_op", 'SUBSURF')
        return {'FINISHED'}
    

#def register(): 
    #bpy.utils.register_class(QuantumMesh_Operator)
    #bpy.utils.register_class(NumberOfVerts)


#def unregister(): 
 #   bpy.utils.unregister_class(QuantumMesh_Operator)
  #  bpy.utils.unregister_class(NumberOfVerts)


# if __name__ == "__main__":
#     register()

