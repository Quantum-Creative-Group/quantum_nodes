import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

class TestExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_extension_menu"
    bl_label = "Quantic Extension Menu"

    def draw(self, context):
        layout = self.layout
        # ADD your node with its bl_idname and bl_label
        insertNode(layout, "an_MeshToHeight", "Mesh to Height")
        insertNode(layout, "an_HeightToMesh", "Height to Mesh")
        insertNode(layout, "an_InitClassicalRegisterNode", "Init Classical Register")
        insertNode(layout, "an_InitQuantumRegisterNode", "Init Quantum Register")
        insertNode(layout, "an_InitQuantumCircuitNode", "Init Quantum Circuit")
        insertNode(layout, "an_QuantumGateHToAllNode", "Quantum GateH To All Circuit")
        insertNode(layout, "an_QuantumGateXToAllNode", "Quantum GateX To All Circuit")
        insertNode(layout, "an_QuantumGateYToAllNode", "Quantum GateY To All Circuit")
        insertNode(layout, "an_QuantumCircuitOutputStateNode", "Quantum Circuit Output State")
        insertNode(layout, "an_QuantumCircuitIBMOutputStateNode", "Quantum Circuit IBM Output State")
                

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