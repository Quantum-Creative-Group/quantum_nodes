from bpy.types import Menu

from animation_nodes.ui.node_menu import insertNode


class QuantumBlurSubmenu(Menu):
    """Menu of Quantum Blur nodes."""

    bl_idname = "AN_MT_quantum_qu_blur"
    bl_label = "Quantum Blur"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumBlurInputNode", "Quantum Blur Input")
        insertNode(layout, "an_QuantumBlurOutputNode", "Quantum Blur Output")
