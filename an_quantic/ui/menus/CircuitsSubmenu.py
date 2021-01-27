from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode

class CircuitsSubmenu(Menu):
    bl_idname = "AN_MT_quantum_init_qu_circuit"
    bl_label = "Init Quantum Circuit"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_InitClassicalRegisterNode", "Init Classical Register")
        insertNode(layout, "an_InitQuantumRegisterNode", "Init Quantum Register")
        insertNode(layout, "an_InitQuantumCircuitNode", "Init Quantum Circuit")