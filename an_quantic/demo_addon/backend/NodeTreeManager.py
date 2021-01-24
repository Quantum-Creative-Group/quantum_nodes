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
        """
        Generates the demo node trees
        """
        genereateMultiplyAll(bpy.ops.node, self.demo_id)
        generateMaxValue(bpy.ops.node, self.demo_id)
        generateNegative(bpy.ops.node, self.demo_id)
        generateMeshData(bpy.ops.node, self.demo_id)
        for circ_name in ["x", "y", "z"]:
            generateCircuit(bpy.ops.node, self.demo_id, circ_name)
        generateMainNodeTree(bpy.ops.node, self.main_tree_id, obj)
        self.node_tree = bpy.data.node_groups[self.main_tree_id + "an_q"]
    
    def updateTarget(self, obj):
        """
        Updates the target of the quantum circuits
        """
        self.node_tree.nodes[self.main_tree_id + "mesh_obj_input" + "_main"].inputs[0].object = obj
        self.node_tree.nodes[self.main_tree_id + "obj_instancer" + "_main"].inputs[1].object = obj
    
    def update(self, new_circuits):
        """
        Updates the circuit node trees
        """
        modif = self.getModification(self.last_circuits, new_circuits)
        if(modif != (None, None, None)):
            circuit_node_tree = bpy.data.node_groups[self.demo_id + "circuit_" + modif[2][0]]
            circuit_id = "_c" + modif[2][0]
            gate_name = self.demo_id + "gate_" + modif[1] + circuit_id
            if(modif[0] == "ADD"):
                new_gate = self.gf.createGate(gate_name, modif[1], modif[2][2], circuit_node_tree)
                print(new_gate)
                existing_gate = self.getExistingGate(circuit_node_tree, new_gate)
                if(existing_gate == None):
                    # add a new gate
                    existing_gates = self.gf.getExistingGates(circuit_node_tree)
                    if(len(existing_gates) > 0):
                        # if there is a gate before
                        gate_node_before = existing_gates[-1]
                        self.removeLink(gate_node_before.outputs[0], new_gate.output.inputs[0], circuit_node_tree)
                    self.addGate(new_gate, circuit_node_tree, modif[2][1])
                else:
                    # the gate already exists
                    existing_gate.newInputSocket()
                    # forces to update the tree (magic trick)
                    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
                    existing_gate.inputs[len(existing_gate.inputs) - 2].value = modif[2][1]
            elif(modif[0] == "DEL"):
                # delete a gate
                if(self.gateIsStillUsed(modif[1], new_circuits[modif[2][0]])):
                    # the gate is still used
                    print("GATE " + modif[1].upper() + " : still used")
                else:
                    # the gate isn't used anymore
                    current_gate_node = circuit_node_tree.nodes[self.demo_id + "gate_" + modif[1] + circuit_id]
                    self.removeGate(current_gate_node, circuit_node_tree)

        # sets last ciruits to the current circuits
        self.last_circuits = copy.deepcopy(new_circuits)

    def resetAllGates(self):
        for circ_name in ["x", "y", "z"]:
            circuit_node_tree = bpy.data.node_groups[self.demo_id + "circuit_" + circ_name]
            for gate_node in circuit_node_tree.nodes:
                if("gate" in gate_node.name):
                    self.removeGate(gate_node, circuit_node_tree)
            

    def addGate(self, new_gate, circuit_tree, q_index):
        """
        Adds a new gate in the given circuit node tree
        """
        circuit_tree.nodes.new(type="an_QuantumGate" + new_gate.type + "Node")
        gate_node = circuit_tree.nodes["Quantum Gate " + new_gate.type]
        gate_node.name = new_gate.name
        gate_node.location = new_gate.location
        gate_node.inputs[0].value = q_index
        circuit_tree.links.new(new_gate.input.outputs[0], gate_node.inputs[1])
        circuit_tree.links.new(gate_node.outputs[0], new_gate.output.inputs[0])
    
    def removeGate(self, gate_node, circuit_tree):
        # save the input and output
        inp = gate_node.originNodes[0].outputs[0]
        out = gate_node.outputs[0].directTargets[0]
        self.removeLink(gate_node.originNodes[0].outputs[0], gate_node.inputs[len(gate_node.inputs) - 1], circuit_tree)
        self.removeLink(gate_node.outputs[0], gate_node.outputs[0].directTargets[0], circuit_tree)
        # link the saved output and input
        circuit_tree.links.new(inp, out)
        gate_node.remove()
        # forces to update the tree (magic trick)
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
    
    @classmethod
    def getModification(cls, last_circuits, new_circuits):
        """
        Returns the informations about the modification done on the circuits

        Returns : action, gate_type, (circuit name, qubit index, gate index)
        """
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
    def getExistingGate(cls, circuit_tree, gate):
        """
        Returns True if the given gate already exists in the node tree
        """
        for node in circuit_tree.nodes:
            if("gate_" + gate.type.lower() in node.name):
                if("index_" + str(gate.index) in node.name or "index_" + str(gate.index - 1) in node.name):
                    return node
        return None
    
    @classmethod
    def removeLink(cls, inp, out, node_tree):
        """
        Removes the link between the given input and output
        """
        for link in node_tree.links:
            if(link.from_socket == inp and link.to_socket == out):
                node_tree.links.remove(link)
    
    @classmethod
    def gateIsStillUsed(cls, gate_type, circuit):
        """
        Returns True if the given gate type is still used in the circuit
        """
        for qubit in circuit.data:
            for gate in qubit:
                if gate == gate_type:
                    return True
        return False
