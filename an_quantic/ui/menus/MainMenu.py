import bpy, os
import bpy.utils.previews
from bpy.types import Menu
from animation_nodes.utils.nodes import getAnimationNodeTrees

def drawMenu(self, context):
    pcoll = preview_collections["main"]
    my_icon = pcoll["my_icon"]
    

    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0: return

    layout.separator()
    layout.menu("AN_MT_quantum_nodes_menu", text = "Quantum Nodes", icon_value = my_icon.icon_id)

class MainMenu(Menu):
    bl_idname = "AN_MT_quantum_nodes_menu"
    bl_label = "Quantum Nodes"
    
    def draw(self, context):
        pcoll = preview_collections["main"]
        complex_icon = pcoll["c_icon"]
        layout = self.layout
        layout.menu("AN_MT_quantum_gates", text = "Quantum Gates", icon = "SHADING_BBOX")
        layout.menu("AN_MT_complex", text = "Complex Numbers", icon_value = complex_icon.icon_id)
        layout.separator()
        layout.menu("AN_MT_quantum_qu_blur", text = "Quantum Blur", icon = "ORIENTATION_VIEW")
        layout.menu("AN_MT_quantum_init_qu_circuit", text = "Init Quantum Circuit", icon = "KEYINGSET")
        layout.menu("AN_MT_quantum_qu_output", text = "Quantum Output", icon = "ORIENTATION_NORMAL")
        layout.separator()
        layout.menu("AN_MT_schrodinger_simulation", text = "Schrödinger Simulation", icon = "OPTIONS")

preview_collections = {}

def register():
    bpy.types.NODE_MT_add.append(drawMenu)
    pcoll = bpy.utils.previews.new()
    # path to the folder where the icons aren. Computes the path relatively this py file
    my_icons_dir = os.path.join(os.path.dirname(__file__), "../icons")
    # loads a preview thumbnail of a file and stores it in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "quantum_nodes.png"), 'IMAGE')
    pcoll.load("c_icon", os.path.join(my_icons_dir, "complex_c.png"), 'IMAGE')
    preview_collections["main"] = pcoll

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()