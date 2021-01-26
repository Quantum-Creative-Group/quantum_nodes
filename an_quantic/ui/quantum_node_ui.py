import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees
from .. node_templates.template1 import *
from . nodes_menu import *
from .. demo_addon.operators.ConnexionIBM import *



class InsertNodeUI(bpy.types.Panel):
    bl_label = "Quantum Node Panel"
    bl_idname = "AN_PT_InsertNodeUI"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "QuantumNode"

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()

        pcoll = preview_collections["main"]
        qubit = pcoll["qubit"]

        row = box.row()
        row.label(text="Templates", icon='EXPERIMENTAL')
        row = box.row()
        row.operator('nodes.insert', text='Wootton QB', icon="TRACKING")
        row.operator('nodes.insert', text='Bloch Sphere', icon="SPHERE")
        
        box = layout.box()
        row = box.row()
        row.label(text="Nodes", icon='NODE')
        row = box.row()
        row.menu("AN_MT_quantic_gates", text = "Gates", icon = "SHADING_BBOX")
        row.menu("AN_MT_quantic_complex", text = "Complex Nb", icon_value=qubit.icon_id)
        row = box.row()
        row.menu("AN_MT_quantic_qu_heightmap", text = "Heightmap", icon = "ORIENTATION_VIEW")
        row.menu("AN_MT_quantic_init_qu_circuit", text = "Init Circuit", icon = "KEYINGSET")
        row = box.row()
        row.menu("AN_MT_quantic_qu_output", text = "Qu Output", icon = "ORIENTATION_NORMAL")
        row.menu("AN_MT_quantic_schrodinger_simulation", text = "Schrödinger", icon = "OPTIONS")


        row = layout.row()
        row = layout.row()



        props = bpy.context.scene.QueryProps

        col = layout.column(align=True)
        rowsub = col.row(align=True)

        rowsub.label(text="Enter your IBM Account token", icon="PREFERENCES")

        rowsub = col.row(align=True)
        rowsub.prop(props, "query", text="")
        rowsub.operator("object.connexion_ibm", text="Query")





        row = layout.row()
        row = layout.row()
        
        row.operator('wm.url_open', text="Need Help ?", icon='BOOKMARKS').url='https://elgoog.im/'

def create_quantum_node_tree(context, operator, gp_name):
    bpy.context.scene.use_nodes = True #use nodes activated
    
    QuantumTree = bpy.ops.node.new_node_tree(name=gp_name)
    
    return QuantumTree

preview_collections = {}

class InsertNodeOP(bpy.types.Operator):
    bl_idname = "nodes.insert"
    bl_label = "Add Quantum Node Tree"

    

    def execute(self, context):
        custom_node_name = "Quantum_Node_Tree 0"
        i = 0
        while bpy.data.node_groups.find((custom_node_name)) != -1 :
            i += 1
            custom_node_name = custom_node_name[: -1]
            custom_node_name += str(i)

        ####---NODES TREE GENERATION---####
        create_quantum_node_tree(context, self, custom_node_name)

        QuGp = bpy.data.node_groups[custom_node_name]

        templateInsertion(context, self, custom_node_name)

        return {'FINISHED'}

#def insertNode(context, operator, node_name):

#def register():
    #bpy.types.NODE_MT_add.append(drawMenu)

#def unregister():
    #bpy.types.NODE_MT_add.remove(drawMenu)

def register():
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')
    pcoll.load("addon_logo", os.path.join(my_icons_dir, "addon_logo.png"), 'IMAGE')
    pcoll.load("qubit", os.path.join(my_icons_dir, "qubit.png"), 'IMAGE')

    preview_collections["main"] = pcoll

    bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProps)

def unregister():
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    del(bpy.types.Scene.QueryProps)