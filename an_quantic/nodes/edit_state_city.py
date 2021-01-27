import bpy
import bmesh
import mathutils
import math
import numpy as np
from qiskit import *
import math
from animation_nodes.base_types import AnimationNode
from .. visualization.state_city_visualization import edit_state_city

class EditStateCityNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_EditStateCityNode"
    bl_label = "Edit State City"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Object", "State City", "state_city")

    def execute(self,quantum_circuit, state_city):
        if state_city is None:
            return
        if (state_city.name != "Quantume_City_Faces") :
            return 
        try:
            backend = Aer.get_backend('statevector_simulator')
            result = execute(quantum_circuit,backend).result() #Do the simulation, returning the result
            out_state = result.get_statevector()

            parent = state_city.parent
            for i in range (len(state_city.children)):
                bpy.data.objects.remove(state_city.children[0])
            bpy.data.objects.remove(state_city)
            edit_state_city(parent,out_state)       
        except:
            return