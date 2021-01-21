import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur
from . circuit_manager import CircuitManager

class QuantumNodes_DEMO_Manager():

    def __init__(self, nb = 1):
        self.qc_x_coords = CircuitManager(nb)
        self.qc_y_coords = CircuitManager(nb)
        self.qc_z_coords = CircuitManager(nb)
        self.selected_circuit = 'x'
        self.nb_qubits = nb

    #def active_object_has_changed(self, obj_name):
    #    if obj_tmp != obj_name: print('OSKOUR')
    def get_selected_circuit(self):
        sc = self.selected_circuit
        if(sc == 'x'): return self.qc_x_coords
        elif(sc == 'y'): return self.qc_y_coords
        return self.qc_z_coords
