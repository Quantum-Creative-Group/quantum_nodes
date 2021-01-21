import bpy
import math
from bpy.props import *
from random import randrange

def QuantumizeIcoSphere(obj): #Disposition random des vertices de l'icosphere
    for vertex in obj.data.vertices:
            vertex.co = [randrange(25)-12.5 for i in range(3)] #A REMPLACER PAR LES PORTES QUANTIQUES


class NumberOfVerts(bpy.types.Operator): #Selection du nombre de subdivisions
    bl_idname = "dialog.number"
    bl_label = "Subdivisions"
    bl_description = "Subdivide your object"
    number = bpy.props.IntProperty(name="subs", default=2, min=1, max=3)

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"

    def execute(self, context):
        obj = bpy.context.active_object
        #if self.number > 10: self.number = 10
        obj.modifiers["My Modifier"].levels = self.number
        #QuantumizeIcoSphere(obj)
        return {'FINISHED'}

    def invoke(self, context, event):    
        return context.window_manager.invoke_props_dialog(self)


class QuantumMesh_Operator(bpy.types.Operator):
    bl_idname = "mesh.quantum_mesh"
    bl_label = "Quantum Mesh"
    bl_description = "Create Quantum Mesh"

    subs = bpy.props.IntProperty(name="subs", default=2, min=1, max=100)

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        obj = bpy.context.active_object
        #print(NumberOfVerts.number)
        mod_subsurf = obj.modifiers.new("My Modifier", 'SUBSURF')
        return {'FINISHED'}
    

#def register(): 
    #bpy.utils.register_class(QuantumMesh_Operator)
    #bpy.utils.register_class(NumberOfVerts)


#def unregister(): 
 #   bpy.utils.unregister_class(QuantumMesh_Operator)
  #  bpy.utils.unregister_class(NumberOfVerts)


if __name__ == "__main__":
    register()

