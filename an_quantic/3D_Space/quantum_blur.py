import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

from bpy.props import(
    BoolProperty,
    FloatProperty,
    PointerProperty,
)
from bpy.types import(
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup,
)

class settings(PropertyGroup):
    
    x_tick: BoolProperty(
        name = "Enable x value",
        description = "Allows the algorithm to include the x value of the coordinate",
        default = False
    )
    y_tick: BoolProperty(
        name = "Enable y value",
        description = "Allows the algorithm to include the y value of the coordinate",
        default = False
    )
    z_tick: BoolProperty(
        name = "Enable z value",
        description = "Allows the algorithm to include the z value of the coordinate",
        default = False
    )
    h_gate_tick: BoolProperty(
        name = "Enable Hadamard gate",
        description = "Allows the algorithm to apply the Hadamard gate",
        default = True
    )
    x_gate_tick: BoolProperty(
        name = "Enable X gate",
        description = "Allows the algorithm to apply the X gate",
        default = False
    )
    y_gate_tick: BoolProperty(
        name = "Enable Y gate",
        description = "Allows the algorithm to apply the Y gate",
        default = False
    )
    distance: FloatProperty(
        name = "Distance",
        description = "Set the distance of the weird point",
        default = 0.0,
        min = 0.0,
        max = 10.0
    )

class quantumize_op(Operator):
    bl_label = "Quantumize"
    bl_idname = "object.quantumize_op"
    bl_description = "Quantumizes the selected mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"
    
    @classmethod
    def mesh2height(self, vertices, index = 0):
        """ Converts a mesh into a python dictionnary containing one of 
        the (x, y, z) coordinates. Uses the exact same logic as James Wootton 
        about QuantumBlur for images, but applied on vertices of a mesh.
        @params :
            vertices : vertices of the mesh
            index : between 0 and 2 (x = 0, y = 1, z = 2)
        """
        nb_vertices = len(vertices)
        # negative_coords is used to get back negative values of coordinates (if there are)
        negative_coords, height = {}, {}
        # size of the dictionnary (n*n) corresponding to the mesh
        n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
        for i in range(n):
            for j in range(n):
                if (i+1)*(j+1) < nb_vertices:
                    # stores absolute value of vertex coord[index]
                    coord = vertices[(i+1)*(j+1)].co[index]
                    height[i,j] = np.abs(coord)
                    if coord > 0: negative_coords[i,j] = 1.0
                    else : negative_coords[i,j] = -1.0
                else:
                    # if the vertex n°(i+1)*(j+1) does not exist
                    height[i,j] = 0.
                    negative_coords[i,j] = 1.0
                    
        return negative_coords, height
    
    @classmethod
    def height2mesh(self, vertices, height, negative_coords, distance, index = 0):
        """ Replaces the vertices by the new ones """
        nb_vertices = len(vertices)
        if distance == 0: distance = 0.00
        n = int(np.sqrt(len(height)))
        for i in range(n):
            for j in range(n):
                if (i+1)*(j+1) < nb_vertices:
                    coord = height[i,j] * negative_coords[i,j] + distance
                    vertices[(i+1)*(j+1)].co[index] = coord
    
    @classmethod
    def transform(self, obj, index, distance, gates):
        negative_coords, height = self.mesh2height(obj.data.vertices, index)
        #print(height)
        #print(negative_coords)
        # Converts heightmap to a qiskit QuantumCircuit
        qc = quantumblur.height2circuit(height)
        # Applies quantum gates to qc
        self.applyQuantumGates(qc, gates)
        # Converts qc back to a heightmap
        new_height = quantumblur.circuit2height(qc)
        # Applies modified vertices to mesh
        self.height2mesh(obj.data.vertices, new_height, negative_coords, distance, index)
    
    @classmethod
    def applyQuantumGates(self, qc, gates): 
        for j in range(qc.num_qubits):
            if gates[0] : qc.h(j)
            if gates[1] : qc.x(j)
            if gates[2] : qc.y(j)
    
    def execute(self, context):
        scene = bpy.context.scene
        settings = scene.quantumize_settings
        
        obj = context.object
        coordinates = [settings.get("x_tick"), settings.get("y_tick"), settings.get("z_tick")]
        gates = [settings.get("h_gate_tick"), settings.get("x_gate_tick"), settings.get("y_gate_tick")]
        for index in range(3):
            if coordinates[index]:
                self.transform(obj, index, settings.get("distance"), gates)
            
        return {'FINISHED'}

class swap_to_an(bpy.types.Operator):
    bl_idname = "screen.swap_to_an"
    bl_label = "Add Material"
    bl_description = "Add New Material"

    def execute(self,context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NODE_EDITOR')
        #if bpy.types.Panel.bl_idname == 'AN_PT_tree_panel': print("coucou")            TESTER SI L'IDNAME CORRESPOND A ANIMATION NODE
        return {'FINISHED'}

        

class quantumize_ui(bpy.types.Panel):
    bl_label = "Quantumize"
    bl_idname = "quantumize_op"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QuantumMesh"
    
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
        row = layout.row()
        row.operator(swap_to_an.bl_idname, text="Advanced", icon="PLUS")

classes = (
    settings,
    quantumize_op,
    quantumize_ui,
)

def register():
#    from bpy.utils import register_class
#    for cls in classes:
#        register_class(cls)
    bpy.types.Scene.quantumize_settings = PointerProperty(type = settings)
#    import sys
#    import os
    # Ajoute le chemin du projet dans sys.path pour pouvoir importer QuantumBlur
#    dir = '/home/theo/Documents/PTut/Blender_Addon/'
#    if not dir in sys.path:
#        sys.path.append(dir)    

#def unregister():
#    for cls in reversed(classes):
#        unregister_class(cls)
#    del bpy.types.Scene.quantumize_settings

if __name__ == "__main__":
    register()

# Deletes meshe(s) that is/are not used in current scene
#for mesh in bpy.data.meshes:
#    if not mesh.users:
#        bpy.data.meshes.remove(mesh)

