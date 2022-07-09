import bpy
import bpy.utils.previews
from bpy.types import Menu

import os

from animation_nodes.utils.nodes import getAnimationNodeTrees


def drawMenu(self, context):
    pcoll = preview_collections["main"]
    qn_icon = pcoll["quantum_nodes_icon"]

    if context.space_data.tree_type != "an_AnimationNodeTree":
        return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0:
        return

    layout.separator()
    layout.menu("QN_MT_quantum_nodes", text="Quantum Nodes", icon_value=qn_icon.icon_id)


class QN_MT_MainMenu(Menu):
    """Main menu of Quantum Nodes."""

    bl_idname = "QN_MT_quantum_nodes"
    bl_label = "Quantum Nodes"

    def draw(self, context):
        pcoll = preview_collections["main"]
        complex_icon = pcoll["complex_icon"]
        layout = self.layout
        layout.menu("QN_MT_init_quantum_circuits", text="Init Quantum Circuit", icon="KEYINGSET")
        layout.menu("QN_MT_quantum_gates", text="Quantum Gates", icon="SHADING_BBOX")
        layout.menu("QN_MT_outputs", text="Quantum Output", icon="ORIENTATION_NORMAL")
        layout.menu("QN_MT_quantum_blur", text="Quantum Blur", icon="ORIENTATION_VIEW")
        # layout.menu("QN_MT_qgan", text = "Quantum GAN", icon = "OPTIONS") # Disable for the moment: WIP
        layout.separator()
        layout.menu("QN_MT_complex_numbers", text="Complex Numbers", icon_value=complex_icon.icon_id)
        layout.separator()
        layout.menu("QN_MT_schrodinger", text="Schrödinger Simulation", icon="OPTIONS")


preview_collections = {}


def register():
    bpy.types.NODE_MT_add.append(drawMenu)
    pcoll = bpy.utils.previews.new()
    # path to the folder where the icons aren. Computes the path relatively this py file
    my_icons_dir = os.path.join(os.path.dirname(__file__), "../icons")
    # loads a preview thumbnail of a file and stores it in the previews collection
    pcoll.load("quantum_nodes_icon", os.path.join(my_icons_dir, "quantum_nodes.png"), 'IMAGE')
    pcoll.load("complex_icon", os.path.join(my_icons_dir, "complex_c.png"), 'IMAGE')
    preview_collections["main"] = pcoll


def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
