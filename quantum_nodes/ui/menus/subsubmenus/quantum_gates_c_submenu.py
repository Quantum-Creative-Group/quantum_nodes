from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode


class QuantumGatsCSubmenu(Menu):
    bl_idname = "AN_MT_quantum_gates_c"
    bl_label = "C Gates"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCHNode", "Quantum Gate CH")
        insertNode(layout, "an_QuantumGateCXNode", "Quantum Gate CX")
        insertNode(layout, "an_QuantumGateCYNode", "Quantum Gate CY")
        insertNode(layout, "an_QuantumGateCZNode", "Quantum Gate CZ")
        insertNode(layout, "an_QuantumGateCCXNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCSWAPNode", "Quantum Gate CSWAP")
