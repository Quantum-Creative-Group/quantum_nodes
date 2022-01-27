from bpy.types import Menu
from animation_nodes.ui.node_menu import insertNode

class QganSubmenu(Menu):
    bl_idname = "AN_MT_quantum_qu_gan"
    bl_label = "Quantum GAN"
    
    def draw(self, context):
        insertNode(self.layout, "an_qGAN", "qGAN Processing")