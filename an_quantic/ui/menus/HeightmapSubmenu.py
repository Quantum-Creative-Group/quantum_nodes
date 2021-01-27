from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode

class HeightmapSubmenu(Menu):
    bl_idname = "AN_MT_quantum_qu_heightmap"
    bl_label = "Quantum Heightmap"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumCircuitToHeightmapNode", "Quantum Circuit To Heightmap")
        insertNode(layout, "an_HeightmapToQuantumCircuitNode", "Heightmap To Quantum Circuit")