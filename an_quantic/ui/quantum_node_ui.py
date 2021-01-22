import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees
from .. node_templates.template1 import *



class InsertNodeUI(bpy.types.Panel):
    bl_label = "Quantum Node Panel"
    bl_idname = "AN_PT_InsertNodeUI"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "QuantumNode"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = layout.row()

        col.operator('nodes.insert', text='Insert new node Tree')
        col.operator('wm.url_open', text="Need Help ?", icon='BOOKMARKS').url='https://elgoog.im/'

def create_quantum_node_tree(context, operator, gp_name):
    bpy.context.scene.use_nodes = True #use nodes activated
    
    QuantumTree = bpy.ops.node.new_node_tree(name=gp_name)
    
    return QuantumTree


class InsertNodeOP(bpy.types.Operator):
    bl_idname = "nodes.insert"
    bl_label = "Add Quantum Node Tree"

    

    def execute(self, context):
        custom_node_name = "Quantum_Node_Tree 0"
        i = 0
        while bpy.data.node_groups.find((custom_node_name)) != -1 :
            i += 1
            custom_node_name = custom_node_name[: -1]
            custom_node_name += str(i)

        ####---NODES TREE GENERATION---####
        create_quantum_node_tree(context, self, custom_node_name)

        QuGp = bpy.data.node_groups[custom_node_name]

        templateInsertion(context, self, custom_node_name)

        return {'FINISHED'}

#def insertNode(context, operator, node_name):

#def register():
    #bpy.types.NODE_MT_add.append(drawMenu)

#def unregister():
    #bpy.types.NODE_MT_add.remove(drawMenu)