import bpy
from . Gate import Gate

class GatesFactory:
    def __init__(self, start_left, spacing, demo_id):
        self.start_loc_left = start_left
        self.spacing = spacing
        self.demo_id = demo_id
    
    def createGate(self, gate_name, gate_type, gate_index, circuit_tree):
        """
        Stores all the useful informations to add a new node to the circuit node tree
        Also moves the output nodes to the right if more space is needed
        """
        existing_gates = self.getExistingGates(circuit_tree)
        nb_existing_gates = len(existing_gates)
        location = (self.start_loc_left + self.spacing + nb_existing_gates * self.spacing, 0)
        if(nb_existing_gates > 0):
            gate_index = nb_existing_gates
            inp = existing_gates[-1]
        else:
            inp = circuit_tree.nodes[1]

        circuit_id = gate_name[len(gate_name) - 3:]
        h2c = circuit_tree.nodes[self.demo_id + "hmap_to_qu_cir" + circuit_id]
        c2h = circuit_tree.nodes[self.demo_id + "qu_cir_to_hmap" + circuit_id]
        grp_out = circuit_tree.nodes[self.demo_id + "grp_out" + circuit_id]
        # TODO: not sure that this code should be here (spacing management)
        if(nb_existing_gates + 1 > (c2h.location[0] - h2c.location[0])/self.spacing):
            # moves to the right the output nodes so the node tree is still readable
            c2h.location[0] += self.spacing
            grp_out.location[0] += self.spacing
        elif((c2h.location[0] - h2c.location[0])/self.spacing > nb_existing_gates + 1):
            # if there is more space than needed
            nb_del_space = int((c2h.location[0] - h2c.location[0])/self.spacing - (nb_existing_gates + 1))
            print(nb_del_space)
            for i in range(nb_del_space):
                c2h.location[0] -= self.spacing
                grp_out.location[0] -= self.spacing
        
        out = circuit_tree.nodes[self.demo_id + "qu_cir_to_hmap" + circuit_id]
        return Gate(gate_type.upper(), "index_" + str(gate_index) + "_" + gate_name, gate_index, location, inp, out)
    
    def getExistingGates(self, circuit_tree):
        """
        Returns all the existing gate nodes in the circuit
        """
        existing_gates = []
        for node in circuit_tree.nodes:
            if("gate" in node.name):
                existing_gates.append(node)
        return existing_gates