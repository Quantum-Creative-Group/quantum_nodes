import bpy

class AN_Q_DemoAddonMeshPanel(bpy.types.Panel):
    bl_idname = "AN_Q_PT_DemoAddonMeshPanel"
    bl_label = "Mesh properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AN_Q_DEMO"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = layout.column()
        col.operator('mesh.create_mesh', text='Create a new mesh')
        col.operator('dialog.number')

#def register(): bpy.utils.register_class(QuantumMeshPanel)

#def unregister(): bpy.utils.unregister_class(QuantumMeshPanel)

# if __name__ == "__main__":
#     register()