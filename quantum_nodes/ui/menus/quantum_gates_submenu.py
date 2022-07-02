from bpy.types import Menu

from animation_nodes.ui.node_menu import insertNode


class QuantumGatesSubmenu(Menu):
    """Menu of all quantum gates nodes."""

    bl_idname = "AN_MT_quantum_gates"
    bl_label = "Gates"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateSWAPNode", "Quantum Gate SWAP")
        layout.separator()
        layout.menu("AN_MT_quantum_gates_c", text="C Gates", icon="EVENT_C")
        layout.menu("AN_MT_quantum_gates_r", text="R Gates", icon="EVENT_R")
        # TODO: are these gates necessary now?
        # layout.menu("AN_MT_quantum_gates_to_all", text = "Gates_To_All", icon = "OBJECT_ORIGIN")
        layout.menu("AN_MT_quantum_gates_single_qubit", text="Single_Qubit_Gates", icon="DOT")
