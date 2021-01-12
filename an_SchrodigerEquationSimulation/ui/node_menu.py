import bpy
from animation_nodes.ui.node_menu import insertNode

class TestExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_test_extension_menu"
    bl_label = "Quantum Menu"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SchrodingerEquationSimulation", "Schrödinger Equation Simulation")

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    layout.separator()
    layout.menu("AN_MT_test_extension_menu", text = "Quantum Menu", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)

