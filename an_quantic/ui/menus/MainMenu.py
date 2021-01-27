import bpy, os
import bpy.utils.previews

from bpy.types import (Menu)
import bpy.utils.previews

from typing import Optional

from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

def drawMenu(self, context):
    pcoll = preview_collections["main"]
    my_icon = pcoll["my_icon"]
    
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0: return

    layout.separator()
    layout.menu("AN_MT_quantic_extension_menu", text = "Quantic Extension Menu", icon_value=my_icon.icon_id)

class QuanticExtensionMenu(Menu):
    bl_idname = "AN_MT_quantic_extension_menu"
    bl_label = "Quantic Extension Menu"
    

    def draw(self, context):
        layout = self.layout

        layout.menu("AN_MT_quantic_gates", text = "Quantum Gates", icon = "SHADING_BBOX")
        layout.menu("AN_MT_quantic_complex", text = "Complex Numbers", icon = "MESH_UVSPHERE")
        layout.separator()
        layout.menu("AN_MT_quantic_qu_heightmap", text = "Quantum Heightmap", icon = "ORIENTATION_VIEW")
        layout.menu("AN_MT_quantic_init_qu_circuit", text = "Init Quantum Circuit", icon = "KEYINGSET")
        layout.menu("AN_MT_quantic_qu_output", text = "Quantum Output", icon = "ORIENTATION_NORMAL")
        layout.separator()
        layout.menu("AN_MT_quantic_schrodinger_simulation", text = "Schrödinger Simulation", icon = "OPTIONS")

preview_collections = {}

def register():
    bpy.types.NODE_MT_add.append(drawMenu)
    pcoll = bpy.utils.previews.new()
    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "../icons")
    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')
    preview_collections["main"] = pcoll

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()