from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode

class QuantumGatesToAllSubmenu(Menu):
    bl_idname = "AN_MT_quantum_gates_to_all"
    bl_label = "Gates To All"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateHToAllNode", "Quantum Gate H To All Circuit")
        insertNode(layout, "an_QuantumGateIDToAllNode", "Quantum Gate ID To All Circuit")
        insertNode(layout, "an_QuantumGateSToAllNode", "Quantum Gate S To All Circuit")
        insertNode(layout, "an_QuantumGateSDGToAllNode", "Quantum Gate SDG To All Circuit")
        insertNode(layout, "an_QuantumGateTToAllNode", "Quantum Gate T To All Circuit")
        insertNode(layout, "an_QuantumGateTDGToAllNode", "Quantum Gate TDG To All Circuit")
        insertNode(layout, "an_QuantumGateXToAllNode", "Quantum Gate X To All Circuit")
        insertNode(layout, "an_QuantumGateYToAllNode", "Quantum Gate Y To All Circuit")
        insertNode(layout, "an_QuantumGateZToAllNode", "Quantum Gate Z To All Circuit")