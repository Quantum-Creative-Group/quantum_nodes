import bpy
from bpy.types import Operator

from .. node_templates.template1 import templateInsertion


def createNodeTree(context, operator, gp_name):
    # uses the activated node tree
    context.scene.use_nodes = True
    QuantumTree = bpy.ops.node.new_node_tree(name=gp_name)
    return QuantumTree


class InsertNode(Operator):
    """Generate the example node tree which uses Quantum Blur."""

    bl_idname = "nodes.insert"
    bl_label = "Add Node Tree"
    bl_description = "WIP : QuantumBlur template"

    # WIP operator
    @classmethod
    def poll(cls, context):
        return False

    def execute(self, context):
        custom_node_name = "Quantum_Node_Tree_"
        i = 0
        while bpy.data.node_groups.find(custom_node_name) != -1:
            i += 1
            custom_node_name = custom_node_name[:-1]
            custom_node_name += str(i)

        createNodeTree(context, self, custom_node_name)
        templateInsertion(context, self, custom_node_name)
        return {'FINISHED'}
