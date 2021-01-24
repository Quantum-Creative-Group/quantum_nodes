import bpy
from . DemoNodeTreeUtils import *

class NodeTreeManager:
    def __init__(self):
        self.demo_id = "an_q_demo_"
        self.main_tree_id = "DEMO_TREE_"
        self.node_tree = None
        self.last_circuits = None
    
    def generateNodeTree(self, obj):
        genereateMultiplyAll(bpy.ops.node, self.demo_id)
        generateMaxValue(bpy.ops.node, self.demo_id)
        generateNegative(bpy.ops.node, self.demo_id)
        generateMeshData(bpy.ops.node, self.demo_id)
        for circ_name in ["x", "y", "z"]:
            generateCircuit(bpy.ops.node, self.demo_id, circ_name)
        generateMainNodeTree(bpy.ops.node, self.main_tree_id, obj)
        self.node_tree = bpy.data.node_groups[self.main_tree_id + "an_q"]
    
    def updateTarget(self, obj):
        self.node_tree.nodes[self.main_tree_id + "mesh_obj_input" + "_main"].inputs[0].object = obj
        self.node_tree.nodes[self.main_tree_id + "obj_instancer" + "_main"].inputs[1].object = obj
    
    def updateNodeTree(self, new_circuits):
        return
    
    def addGate(self):
        return
    
    def removeGate(self):
        return
