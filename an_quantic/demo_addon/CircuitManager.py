import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

class CircuitManager():

    def __init__(self, nb_qubits):
        self.data = [[] for i in range(nb_qubits)]

    def add_gate(self, q_index, gate):
        if len(self.data[q_index]) < 6 : 
            self.data[q_index].append(gate)
        print(self.data[q_index])

    def del_gate(self, q_index):
        if len(self.data[q_index]) > 0 : 
            self.data[q_index].pop()
        print(self.data[q_index])
    

        
