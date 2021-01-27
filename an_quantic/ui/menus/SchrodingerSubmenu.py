from bpy.types import (Menu)

from animation_nodes.ui.node_menu import insertNode

class SchrodingerSubmenu(Menu):
    bl_idname = "AN_MT_quantic_schrodinger_simulation"
    bl_label = "Schrödinger Simulation"
    
    def draw(self, context):
        insertNode(self.layout, "an_SchrodingerEquationSimulation", "Schrödinger Equation Simulation")