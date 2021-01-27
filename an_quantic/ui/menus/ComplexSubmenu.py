from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class ComplexSubmenu(Menu):
    bl_idname = "AN_MT_quantic_complex"
    bl_label = "Complex Numbers"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SplitComplex128", "Split complex128")