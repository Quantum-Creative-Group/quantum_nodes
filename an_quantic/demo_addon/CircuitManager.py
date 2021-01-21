import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

class CircuitManager():

    def __init__(self, nb_qubits):
        self.data = [[] for i in range(nb_qubits)]

    def add_gate(self, q_index, gate):
       if len(self.data[q_index]) < 5 : 
            ###### DISABLE CURRENT OBJ
            tmp = bpy.context.active_object.name
            bpy.context.active_object.select_set(False)
            
            ###### APPEND GATE
            self.data[q_index].append(gate)
            
            ###### ENABLE OBJ 
            bpy.data.objects[tmp].select_set(True)  
        
            ##### TADAAAAAAAAAAA CALL ME HOUDINI
        #print(self.data[q_index])

    def del_gate(self, q_index):
        if len(self.data[q_index]) > 0 : 
            self.data[q_index].pop()
        

        
