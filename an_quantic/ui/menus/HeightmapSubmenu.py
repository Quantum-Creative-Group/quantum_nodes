from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class HeightmapSubmenu(Menu):
    bl_idname = "AN_MT_quantic_qu_heightmap"
    bl_label = "Quantum Heightmap"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_MeshToHeight", "Mesh to Height")
        insertNode(layout, "an_HeightToMesh", "Height to Mesh")
        insertNode(layout, "an_QuantumCircuitToHeightmapNode", "Quantum Circuit To Heightmap")
        insertNode(layout, "an_HeightmapToQuantumCircuitNode", "Heightmap To Quantum Circuit")