import bpy, os, sys

from . CircuitManager import CircuitManager
from . NodeTreeManager import NodeTreeManager

class QuantumNodes_DEMO_Manager():

    def __init__(self, nb = 3):
        self.qc_x_coords = CircuitManager(nb)
        self.qc_y_coords = CircuitManager(nb)
        self.qc_z_coords = CircuitManager(nb)
        self.selected_circuit = 'x'
        self.ntm = NodeTreeManager()
        self.nb_qubits = nb
        self.initialized = False
        self.selected_obj = None
        
    def get_selected_circuit(self):
        sc = self.selected_circuit
        if(sc == 'x'): return self.qc_x_coords
        elif(sc == 'y'): return self.qc_y_coords
        return self.qc_z_coords
    
    def initializeDemo(self):
        if(not self.initialized):
            self.ntm.generateNodeTree()
            self.initialized = True
