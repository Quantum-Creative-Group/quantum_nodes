import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

class CircuitManager():

    def __init__(self, nb_qubits):
        self.data = [[] for i in range(nb_qubits)]

    def add_gate(self, q_index, gate):
        print(self)
        if len(self.data[q_index]) < 5 : 
            self.data[q_index].append(gate)
        #print(len(self.data[q_index]))
        print(self.data[q_index])

    def del_gate(self, q_index):
        if len(self.data[q_index]) > 0 : 
            self.data[q_index].pop()
        print(self.data[q_index])
    

        
