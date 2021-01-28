import bpy
from bpy.types import Operator
from ... node_templates.template1 import templateInsertion

def create_quantum_node_tree(context, operator, gp_name):
    bpy.context.scene.use_nodes = True # use nodes activated
    
    QuantumTree = bpy.ops.node.new_node_tree(name=gp_name)
    
    return QuantumTree

class InsertNodeOP(Operator):
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

        # QuGp = bpy.data.node_groups[custom_node_name]

        templateInsertion(context, self, custom_node_name)

        return {'FINISHED'}