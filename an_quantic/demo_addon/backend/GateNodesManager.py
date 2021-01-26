import bpy

class GateNodesManager:

    @classmethod
    def addGate(cls, new_gate, circuit_tree, q_index):
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
    
    @classmethod
    def removeGate(cls, gate_node, circuit_tree):
        """
        Removes the given gate node
        Creates a new link between the input and output of the deleted node
        """
        # saves the input and output
        inp = gate_node.originNodes[0].outputs[0]
        out = gate_node.outputs[0].directTargets[0]
        cls.removeLink(gate_node.originNodes[0].outputs[0], gate_node.inputs[len(gate_node.inputs) - 1], circuit_tree)
        cls.removeLink(gate_node.outputs[0], gate_node.outputs[0].directTargets[0], circuit_tree)
        # links the saved output and input
        circuit_tree.links.new(inp, out)
        gate_node.remove()
        # forces to update the tree (magic trick)
        # TODO: find a better solution
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)

    @classmethod
    def getExistingGate(cls, circuit_tree, gate_type, q_index, qubit_data):
        """
        Returns the gate if it already exists
        """
        # finds the first node that contains a gate of the corresponding circuit
        # so let's start looking from this index for a potential existing gate
        min_gate_index = 0
        if(len(qubit_data) > 0):
            # only when there are already gates in the node tree
            for node in circuit_tree.nodes:
                if("gate_" in node.name):
                    if(not cls.qubitIndexInGate(q_index, node)):
                        min_gate_index += 1
                    else:
                        break
        
        # finds where the potential existing gate should (at least) 
        # be placed from the previous min_gate_index
        last_gate_type = "" # last_gate_type is used to counter redundancy (ex: q1 --|H|--|H|--)
        for g in qubit_data:
            if(g != gate_type and last_gate_type != g):
                min_gate_index += 1
            last_gate_type = g

        # searches for the potential existing gate with these conditions :
        # gate_index >= min_gate_index and "gate_T" in node.name
        gate_index = 0
        for node in circuit_tree.nodes:
            if("gate_" in node.name):
                if("gate_" + gate_type in node.name):
                    if(gate_index >= min_gate_index):
                        return node
                gate_index += 1

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
    def qubitIndexInGate(cls, q_index, node):
        """
        Returns True if the q_index is a value of one of the sockets
        """
        for socket in node.inputs:
            if(type(socket).__name__ == "IntegerSocket" and q_index == socket.value):
                return True
        return False