import bpy

class QuantumMeshPanel(bpy.types.Panel):
    bl_idname = "QuantumMeshPanel"
    bl_label = "Quantum Mesh Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QuantumMesh"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = layout.column()
        col.operator('mesh.quantum_mesh', text='Create Quantum Mesh')
        col.operator('dialog.number')
        #col.operator('screen.swap_to_an')
        #col.operator('object.quantumize_ui')

#def register(): bpy.utils.register_class(QuantumMeshPanel)

#def unregister(): bpy.utils.unregister_class(QuantumMeshPanel)

if __name__ == "__main__":
    register()