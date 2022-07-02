from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode


class QuantumGatsRSubmenu(Menu):
    """Menu of R gates nodes."""

    bl_idname = "AN_MT_quantum_gates_r"
    bl_label = "R Gates"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateRXNode", "Quantum Gate RX")
        insertNode(layout, "an_QuantumGateRYNode", "Quantum Gate RY")
        insertNode(layout, "an_QuantumGateRZNode", "Quantum Gate RZ")
