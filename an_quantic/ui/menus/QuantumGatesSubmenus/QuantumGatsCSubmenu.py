from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class QuanticExtensionMenu_Gates_c(Menu):
    bl_idname = "AN_MT_quantic_gates_c"
    bl_label = "Gates_C"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCHNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCXNode", "Quantum Gate CX")
        insertNode(layout, "an_QuantumGateCYNode", "Quantum Gate CY")
        insertNode(layout, "an_QuantumGateCZNode", "Quantum Gate CZ")