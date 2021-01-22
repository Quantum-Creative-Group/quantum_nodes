import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees
from . DemoNodeTreeUtils import *

class NodeTreeManager:
    def __init__(self):
        self.target_node_tree = "DEMO_TREE"
        self.last_circuits = None
    
    def generateNodeTree(self):
        generateCircuit(bpy.ops.node, "an_q_demo_", "x")
    
    def updateNodeTree(self, new_circuits):
        return
    
    def addGate(self):
        return
    
    def removeGate(self):
        return
