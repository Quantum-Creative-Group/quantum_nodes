import bpy
import copy
from . DemoNodeTreeUtils import *
from . GatesFactory import GatesFactory

class NodeTreeManager:
    def __init__(self):
        self.demo_id = "an_q_demo_"
        self.main_tree_id = "DEMO_TREE_"
        self.node_tree = None
        self.last_circuits = None
        self.gf = GatesFactory(self.demo_id)
    
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
    
    def update(self, new_circuits):
        modif = self.getModification(self.last_circuits, new_circuits)
        if(modif != (None, None, None)):
            circuit_node_tree = bpy.data.node_groups[self.demo_id + "circuit_" + modif[2][0]]
            circuit_id = "_c" + modif[2][0]
            gate_name = self.demo_id + "gate_" + modif[1] + circuit_id
            if(modif[0] == "ADD"):
                if(not self.gateAlreadyExists(circuit_node_tree, gate_name)):
                    # add a new gate
                    new_gate_node = self.gf.createGate(gate_name, modif[1], circuit_node_tree)
                    existing_gates = self.gf.getExistingGates(circuit_node_tree)
                    if(len(existing_gates) > 0):
                        # if there is a gate before
                        gate_node_before = existing_gates[-1]
                        self.removeLink(gate_node_before.outputs[0], new_gate_node.output.inputs[0], circuit_node_tree)
                    self.addGate(new_gate_node, circuit_node_tree, modif[2][1])
                else:
                    # the gate already exists
                    current_gate = circuit_node_tree.nodes[self.demo_id + "gate_" + modif[1] + circuit_id]
                    current_gate.newInputSocket()
                    # forces to update the tree (magic trick)
                    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
                    print(len(current_gate.inputs) - 1, modif[2][1])
                    current_gate.inputs[len(current_gate.inputs) - 2].value = modif[2][1]
            elif(modif[0] == "DEL"):
                print("DEL")
            print(modif)
        self.last_circuits = copy.deepcopy(new_circuits)
    
    @classmethod
    def getModification(cls, last_circuits, new_circuits):
        # returns : action, gate_type, (circuit name, qubit index, gate index)
        for circ_name in ["x", "y", "z"]:
            q_index = 0
            for qubit in new_circuits[circ_name].data:
                if(len(qubit) > len(last_circuits[circ_name].data[q_index])):
                    # the user pushed a new gate
                    return "ADD", qubit[-1], (circ_name, q_index, len(qubit) -1)
                elif(len(qubit) < len(last_circuits[circ_name].data[q_index])):
                    # the user deleted a gate
                    last_qubit = last_circuits[circ_name].data[q_index]
                    return "DEL", last_qubit[-1], (circ_name, q_index, len(last_qubit) - 1)
                q_index += 1
        return None, None, None
    
    @classmethod
    def gateAlreadyExists(cls, circuit_tree, gate_name):
        """
        Returns True if the given gate already exists in the node tree
        """
        print(circuit_tree, gate_name)
        try:
            gate = circuit_tree.nodes[gate_name]
            return True
        except:
            return False

    def addGate(self, new_gate, circuit_tree, q_index):
        circuit_tree.nodes.new(type="an_QuantumGate" + new_gate.type + "Node")
        gate_node = circuit_tree.nodes["Quantum Gate " + new_gate.type]
        gate_node.name = new_gate.name
        gate_node.location = new_gate.location
        gate_node.inputs[0].value = q_index
        circuit_tree.links.new(new_gate.input.outputs[0], gate_node.inputs[1])
        circuit_tree.links.new(gate_node.outputs[0], new_gate.output.inputs[0])
        return
    
    @classmethod
    def removeLink(cls, inp, out, node_tree):
        for link in node_tree.links:
            if(link.from_socket == inp and link.to_socket == out):
                node_tree.links.remove(link)
    
    def removeGate(self):
        return
