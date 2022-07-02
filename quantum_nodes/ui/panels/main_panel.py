import bpy
import os
import bpy.utils.previews
from bpy.types import Panel
from animation_nodes.ui.node_menu import insertNode
from .. properties.query_properties import QueryProperties


class MainPanel(Panel):
    """Main panel of Quantum Nodes."""

    bl_label = "Quantum Nodes"
    bl_idname = "AN_PT_MainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Quantum Nodes"

    # TODO: tries to load your account if it's already saved on your computer
    # def __init__(self):
    #     try:
    #         IBMQ.load_account()
    #         bpy.context.scene.QueryProps.connected = True
    #     except Exception as e:
    #         print(e.args)

    def draw(self, context):
        layout = self.layout

        # icons
        pcoll = preview_collections["main"]
        complex_icon = pcoll["complex_icon"]

        # tools
        box = layout.box()
        row = box.row()
        row.label(text="Tools", icon='TOOL_SETTINGS')
        row = box.row()
        row.operator('nodes.insert', text='Wootton QB', icon="TRACKING")
        row.operator('object.bloch_sphere_instancer', text='Bloch sphere', icon="SPHERE")
        row = box.row()
        row.operator('object.histogram_instancer', text='Histogram', icon="SEQ_HISTOGRAM")
        row.operator('object.state_city_instancer', text='State City', icon="SNAP_VERTEX")
        row = box.row()
        row.operator('object.qgan_histogram_instancer', text='qGAN Histogram', icon="SEQ_HISTOGRAM")

        # menu
        box = layout.box()
        row = box.row()
        row.label(text="Nodes", icon='NODE')
        row = box.row()
        row.menu("AN_MT_quantum_gates", text="Gates", icon="SHADING_BBOX")
        row.menu("AN_MT_complex", text="Complex Nb", icon_value=complex_icon.icon_id)
        row = box.row()
        row.menu("AN_MT_quantum_qu_blur", text="Qu Blur", icon="ORIENTATION_VIEW")
        row.menu("AN_MT_quantum_init_qu_circuit", text="Init Circuit", icon="KEYINGSET")
        row = box.row()
        row.menu("AN_MT_quantum_all_qu_output", text="Qu Output", icon="ORIENTATION_NORMAL")
        row.menu("AN_MT_schrodinger_simulation", text="Schrödinger", icon="OPTIONS")
        # row = box.row()
        # row.menu("AN_MT_quantum_all_qu_output", text = "qGAN", icon = "OPTIONS")
        row = layout.row()
        row = layout.row()

        # IMBQ API connection
        props = bpy.context.scene.QueryProps

        col = layout.column(align=True)
        rowsub = col.row(align=True)
        rowsub.label(text="Enter your IBM Account token", icon="PREFERENCES")
        rowsub = col.row(align=True)
        rowsub.prop(props, "query", text="")
        rowsub.operator("object.ibm_connexion", text="Query")

        if props.connected:
            box = layout.box()
            row = box.row()
            row.label(text="Connected", icon="CHECKMARK")
        if props.error_msg != "":
            box = layout.box()
            row = box.row()
            row.label(text=props.error_msg, icon="ERROR")

        # help button
        row = layout.row()
        row = layout.row()
        row.operator(
            'wm.url_open',
            text="Need Help ?",
            icon='BOOKMARKS').url = 'https://quantum-creative-group.gitlab.io/quantum_nodes_manual/'
        row = layout.row()
        row.operator(
            'wm.url_open',
            text="Creation gallery",
            icon='FUND').url = 'https://www.instagram.com/quantumnodes/'


preview_collections = {}


def register():
    pcoll = bpy.utils.previews.new()
    # path to the folder where the icons aren. Computes the path relatively this py file
    my_icons_dir = os.path.join(os.path.dirname(__file__), "../icons")
    # loads a preview thumbnail of a file and stores it in the previews collection
    pcoll.load("complex_icon", os.path.join(my_icons_dir, "complex_c.png"), 'IMAGE')
    preview_collections["main"] = pcoll

    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProperties)


def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    del(bpy.types.Scene.QueryProps)
