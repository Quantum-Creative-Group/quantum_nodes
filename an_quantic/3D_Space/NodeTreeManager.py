import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

class NodeTreeManager:
    def __init__(self):
        self.target_node_tree = "DEMO_TREE"
        self.last_circuits = None
    
    def generateNodeTree(self):
        bpy.ops.node.new_node_tree(type="an_AnimationNodeTree", name=self.target_node_tree)
        node_tree = bpy.data.node_groups[self.target_node_tree]
    
    def updateNodeTree(self, new_circuits):
        return
    
    def addGate(self):
        return
    
    def removeGate(self):
        return
