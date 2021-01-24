import bpy
from . Gate import Gate

class GatesFactory:
    def __init__(self, did):
        self.start_loc_left = -200
        self.spacing = 250
        self.demo_id = did
    
    def createGate(self, gate_name, gate_type, gate_index, circuit_tree):
        existing_gates = self.getExistingGates(circuit_tree)
        nb_existing_gates = len(existing_gates)
        location = (self.start_loc_left + self.spacing + nb_existing_gates * self.spacing, 0)
        if(nb_existing_gates > 0):
            inp = existing_gates[-1]
            gate_index = nb_existing_gates
        else:
            inp = circuit_tree.nodes[1]
        out = circuit_tree.nodes[self.demo_id + "qu_cir_to_hmap" + gate_name[len(gate_name) - 3:]]
        return Gate(gate_type.upper(), "index_" + str(gate_index) + "_" + gate_name, gate_index, location, inp, out)
    
    def getExistingGates(self, circuit_tree):
        existing_gates = []
        for node in circuit_tree.nodes:
            if("gate" in node.name):
                existing_gates.append(node)
        return existing_gates