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
    number = bpy.props.IntProperty(name = " Number Of Subdivisions : ")

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"

    def execute(self, context):
        obj = bpy.context.active_object
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
    def draw(self, context):
        # variables
        layout = self.layout
        scene = context.scene
        obj = context.object
        settings = scene.quantumize_settings
        
        row = layout.row()
        row.label(text="Objet sélectionné", icon="MESH_CUBE")
        row = layout.row()
        row.prop(obj, "name")
        row = layout.row()
        row.label(text="Paramètres", icon="ORIENTATION_LOCAL")
        row = layout.row()
        row.prop(settings, "x_tick", text = "X")
        row.prop(settings, "y_tick", text = "Y")
        row.prop(settings, "z_tick", text = "Z")
        row = layout.row()
        row.prop(settings, "distance")
        row = layout.row()
        row.prop(settings, "h_gate_tick", text = "H gate")
        row.prop(settings, "x_gate_tick", text = "X gate")
        row.prop(settings, "y_gate_tick", text = "Y gate")
        row = layout.row()
        row.operator(quantumize_op.bl_idname, text="Appliquer", icon="CHECKMARK")

    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        obj = bpy.context.active_object
        #print(NumberOfVerts.number)
        mod_subsurf = obj.modifiers.new("My Modifier", 'SUBSURF')
        return {'FINISHED'}

class SwapToAN(bpy.types.Operator):
    bl_idname = "screen.swap_to_an"
    bl_label = "Add Material"
    bl_description = "Add New Material"

    def execute(self,context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NODE_EDITOR')
        #if bpy.types.Panel.bl_idname == 'AN_PT_tree_panel': print("coucou")            TESTER SI L'IDNAME CORRESPOND A ANIMATION NODE
        return {'FINISHED'}

    

#def register(): 
    #bpy.utils.register_class(QuantumMesh_Operator)
    #bpy.utils.register_class(NumberOfVerts)


#def unregister(): 
 #   bpy.utils.unregister_class(QuantumMesh_Operator)
  #  bpy.utils.unregister_class(NumberOfVerts)


if __name__ == "__main__":
    register()

