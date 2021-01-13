import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

class TestExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_extension_menu"
    bl_label = "Quantic Extension Menu"

    def draw(self, context):
        layout = self.layout
        # REPLACE with bl_idname and bl_label of the node in the nodes folder
        insertNode(layout, "an_CopyLocationWithOffsetNode", "Copy Location with Offset")
        insertNode(layout, "an_MeshToHeight", "Mesh to Height")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0: return

    layout.separator()
    layout.menu("AN_MT_quantic_extension_menu", text = "Quantic Extension Menu", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)