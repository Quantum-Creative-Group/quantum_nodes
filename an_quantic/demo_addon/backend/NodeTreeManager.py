import bpy
import copy

from . DemoNodeTreeUtils import *
from . GatesFactory import GatesFactory
from . GateNodesManager import GateNodesManager


class NodeTreeManager:
    def __init__(self):
        self.demo_id = "an_q_demo_"
        self.main_tree_id = "DEMO_TREE_"
        self.main_node_tree = None
        self.last_circuits = None
        self.gf = GatesFactory(-200, 250, self.demo_id)
    
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
        self.main_node_tree = bpy.data.node_groups[self.main_tree_id + "an_q"]
    
    def updateTarget(self, obj):
        """
        Updates the target of the quantum circuits
        """
        self.main_node_tree.nodes[self.main_tree_id + "mesh_obj_input" + "_main"].inputs[0].object = obj
        self.main_node_tree.nodes[self.main_tree_id + "obj_instancer" + "_main"].inputs[1].object = obj
    
    def update(self, new_circuits):
        """
        Updates the circuit node trees
        If "ADD" : 
            Searches for a potential existing gate to insert the new one
            If not found, then creates a new node
        If "DEL" :
            Retrieves the node where the gate is and removes the socket
            If the node isn't used anymore, deletes it
        """
        # detects the modification
        modif = self.getModification(self.last_circuits, new_circuits)
        if(modif != (None, None, None)):
            # identifies the node tree and builds the name of the gate
            circuit_node_tree = bpy.data.node_groups[self.demo_id + "circuit_" + modif[2][0]]
            circuit_id = "_c" + modif[2][0]
            gate_name = self.demo_id + "gate_" + modif[1] + circuit_id

            if(modif[0] == "ADD"):
                qubit_data = self.last_circuits[modif[2][0]].data[modif[2][1]] # data before modification
                existing_gate = GateNodesManager.getExistingGate(circuit_node_tree, modif[1], modif[2][1], qubit_data)
                if(existing_gate == None):
                    # add a new gate
                    new_gate = self.gf.createGate(gate_name, modif[1], modif[2][2], circuit_node_tree)
                    existing_gates = self.gf.getExistingGates(circuit_node_tree)
                    if(len(existing_gates) > 0):
                        # if there is a gate before
                        gate_node_before = existing_gates[-1]
                        GateNodesManager.removeLink(gate_node_before.outputs[0], new_gate.output.inputs[0], circuit_node_tree)
                    GateNodesManager.addGate(new_gate, circuit_node_tree, modif[2][1])
                else:
                    # the gate already exists
                    existing_gate.newInputSocket()
                    # forces to update the tree (magic trick)
                    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
                    existing_gate.inputs[len(existing_gate.inputs) - 2].value = modif[2][1]

            elif(modif[0] == "DEL"):
                # delete a gate
                qubit_data = new_circuits[modif[2][0]].data[modif[2][1]] # data before modification      
                existing_gate = GateNodesManager.getExistingGate(circuit_node_tree, modif[1], modif[2][1], qubit_data)
                for socket in existing_gate.inputs:
                    if(type(socket).__name__ == "IntegerSocket" and socket.value == modif[2][1]):
                        socket.remove()
                        break
                # if the gate isn't used anymore
                if(len(existing_gate.inputs) == 1):
                    GateNodesManager.removeGate(existing_gate, circuit_node_tree)

        # sets last ciruits to the current circuits
        self.last_circuits = copy.deepcopy(new_circuits)

    def resetAllGates(self):
        """
        Resets all the gate nodes in the node trees (for each circuit)
        """
        for circ_name in ["x", "y", "z"]:
            circuit_node_tree = bpy.data.node_groups[self.demo_id + "circuit_" + circ_name]
            for gate_node in circuit_node_tree.nodes:
                if("gate" in gate_node.name):
                    GateNodesManager.removeGate(gate_node, circuit_node_tree)
    
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