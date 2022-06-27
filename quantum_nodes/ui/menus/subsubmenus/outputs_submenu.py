from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode


class OutputsSubmenu(Menu):
    bl_idname = "AN_MT_quantum_qu_output"
    bl_label = "Quantum Output"

    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumCircuitGetCountNode", "Quantum Circuit Get Count")
        insertNode(layout, "an_QuantumCircuitOutputStateNode", "Quantum Circuit Output State")
        insertNode(layout, "an_QuantumMeasureNode", "Quantum Measure")
        insertNode(layout, "an_QuantumCircuitIBMOutputStateNode", "Quantum Circuit IBM Output")
