import bpy

class AN_Q_DemoAddonMeshPanel(bpy.types.Panel):
    bl_idname = "AN_Q_PT_DemoAddonMeshPanel"
    bl_label = "Add a new mesh"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QN Demo"

    def draw(self, context):
        row = self.layout.row()
        row.menu("VIEW3D_MT_mesh_add", text = "Meshes", icon = "OUTLINER_OB_MESH")
        row.operator('dialog.number')