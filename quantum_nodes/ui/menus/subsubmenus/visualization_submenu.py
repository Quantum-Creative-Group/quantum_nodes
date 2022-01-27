from bpy.types import (Menu)
from animation_nodes.ui.node_menu import insertNode

class VisualizationSubmenu(Menu):
    bl_idname = "AN_MT_quantum_visualization_tools"
    bl_label = "Visualization tools"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_BlochSphereNode", "Bloch sphere")
        insertNode(layout, "an_HistogramNode", "Histogram")
        insertNode(layout, "an_StateCityNode", "State city")
        insertNode(layout, "an_QganHistogramNode", "qGAN Histogram")