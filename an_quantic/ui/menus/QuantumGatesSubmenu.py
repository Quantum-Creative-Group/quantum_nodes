from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class QuantumGatesSubmenu(Menu):
    bl_idname = "AN_MT_quantic_gates"
    bl_label = "Gates"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCCXNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCSWAPNode", "Quantum Gate CSWAP")
        insertNode(layout, "an_QuantumGateSWAPNode", "Quantum Gate SWAP")
        layout.separator()
        layout.menu("AN_MT_quantic_gates_c", text = "Gates_C", icon = "EVENT_C")
        layout.menu("AN_MT_quantic_gates_r", text = "Gates_R", icon = "EVENT_R")
        layout.menu("AN_MT_quantic_gates_to_all", text = "Gates_To_All", icon = "OBJECT_ORIGIN")
        layout.menu("AN_MT_quantic_gates_single_qubit", text = "Single_Qubit_Gates", icon = "DOT")