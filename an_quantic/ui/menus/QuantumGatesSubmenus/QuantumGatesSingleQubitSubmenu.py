from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class QuanticExtensionMenu_Gates_Single_Qubit(Menu):
    bl_idname = "AN_MT_quantic_gates_single_qubit"
    bl_label = "Single_Qubit_Gates"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateHNode", "Quantum Gate H")
        insertNode(layout, "an_QuantumGateIDNode", "Quantum Gate ID")
        insertNode(layout, "an_QuantumGateSNode", "Quantum Gate S")
        insertNode(layout, "an_QuantumGateSDGNode", "Quantum Gate SDG")
        insertNode(layout, "an_QuantumGateTNode", "Quantum Gate T")
        insertNode(layout, "an_QuantumGateTDGNode", "Quantum Gate TDG")
        insertNode(layout, "an_QuantumGateXNode", "Quantum Gate X")
        insertNode(layout, "an_QuantumGateYNode", "Quantum Gate Y")
        insertNode(layout, "an_QuantumGateZNode", "Quantum Gate Z")