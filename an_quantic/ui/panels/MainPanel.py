import bpy, os
import bpy.utils.previews
from bpy.types import Panel
from animation_nodes.ui.node_menu import insertNode
from .. properties.QueryProperties import QueryProperties

class MainPanel(Panel):
    bl_label = "Quantum Node Panel"
    bl_idname = "AN_PT_MainPanel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Quantum Node"

    # TODO: tries to load your account if it's already saved on your computer
    # def __init__(self):
    #     try:
    #         IBMQ.load_account()
    #         bpy.context.scene.QueryProps.connected = True
    #     except Exception as e:
    #         print(e.args)

    def draw(self, context):
        layout = self.layout
        pcoll = preview_collections["main"]
        qubit = pcoll["qubit"]

        box = layout.box()
        row = box.row()
        row.label(text = "Templates", icon = 'EXPERIMENTAL')
        row = box.row()
        row.operator('nodes.insert', text = 'Wootton QB', icon = "TRACKING")
        row.operator('nodes.insert', text = 'Bloch Sphere', icon = "SPHERE")
        
        box = layout.box()
        row = box.row()
        row.label(text = "Nodes", icon = 'NODE')
        row = box.row()
        row.menu("AN_MT_quantic_gates", text = "Gates", icon = "SHADING_BBOX")
        row.menu("AN_MT_quantic_complex", text = "Complex Nb", icon_value = qubit.icon_id)
        row = box.row()
        row.menu("AN_MT_quantic_qu_heightmap", text = "Heightmap", icon = "ORIENTATION_VIEW")
        row.menu("AN_MT_quantic_init_qu_circuit", text = "Init Circuit", icon = "KEYINGSET")
        row = box.row()
        row.menu("AN_MT_quantic_qu_output", text = "Qu Output", icon = "ORIENTATION_NORMAL")
        row.menu("AN_MT_quantic_schrodinger_simulation", text = "Schrödinger", icon = "OPTIONS")

        row = layout.row()
        row = layout.row()

        props = bpy.context.scene.QueryProps

        col = layout.column(align = True)
        rowsub = col.row(align = True)
        rowsub.label(text = "Enter your IBM Account token", icon="PREFERENCES")
        rowsub = col.row(align = True)
        rowsub.prop(props, "query", text = "")
        rowsub.operator("object.ibm_connexion", text = "Query")
        
        if props.connected:
            box = layout.box()
            row = box.row()
            row.label(text = "Connected", icon = "CHECKMARK")
        if props.error_msg != "":
            box = layout.box()
            row = box.row()
            row.label(text = props.error_msg, icon = "ERROR")

        row = layout.row()
        row = layout.row()
        row.operator('wm.url_open', text = "Need Help ?", icon = 'BOOKMARKS').url = 'https://elgoog.im/'

preview_collections = {}

def register():
    pcoll = bpy.utils.previews.new()
    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "../icons")
    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')
    pcoll.load("addon_logo", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')
    pcoll.load("qubit", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')
    preview_collections["main"] = pcoll
    
    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type = QueryProperties)

def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    del(bpy.types.Scene.QueryProps)