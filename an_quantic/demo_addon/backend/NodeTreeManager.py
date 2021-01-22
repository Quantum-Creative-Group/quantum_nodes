import bpy
from . DemoNodeTreeUtils import *

class NodeTreeManager:
    def __init__(self):
        self.target_node_tree = "DEMO_TREE_"
        self.last_circuits = None
    
    def generateNodeTree(self):
        genereateMultiplyAll(bpy.ops.node, "an_q_demo_")
        generateMaxValue(bpy.ops.node, "an_q_demo_")
        generateNegative(bpy.ops.node, "an_q_demo_")
        generateMeshData(bpy.ops.node, "an_q_demo_")
        generateMainNodeTree(bpy.ops.node, self.target_node_tree)
    
    def updateNodeTree(self, new_circuits):
        return
    
    def addGate(self):
        return
    
    def removeGate(self):
        return
