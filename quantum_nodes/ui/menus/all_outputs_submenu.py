from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode


class AllOutputsSubmenu(Menu):
    """Menu of all output gates nodes."""

    bl_idname = "AN_MT_quantum_all_qu_output"
    bl_label = "All Quantum Output"

    def draw(self, context):
        layout = self.layout
        layout.menu("AN_MT_quantum_visualization_tools", text="Visualization", icon="HIDE_OFF")
        layout.menu("AN_MT_quantum_qu_output", text="Quantum Output", icon="ORIENTATION_NORMAL")
