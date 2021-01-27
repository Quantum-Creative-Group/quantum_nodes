from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class QuantumGatsRSubmenu(Menu):
    bl_idname = "AN_MT_quantic_gates_r"
    bl_label = "Gates_R"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateRXNode", "Quantum Gate RX")
        insertNode(layout, "an_QuantumGateRYNode", "Quantum Gate RY")
        insertNode(layout, "an_QuantumGateRZNode", "Quantum Gate RZ")