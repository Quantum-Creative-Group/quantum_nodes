import bpy
from qiskit import *
import math
import numpy as np
from animation_nodes.base_types import AnimationNode
from qiskit.visualization.utils import _bloch_multivector_data

def get_angles(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    if (r<10**-15):
        theta = 0
        phi = 0
    else :
        theta = np.arccos(z/r)
        if (x==0):
            if(y > 0):
                phi = np.pi/2
            else:
                phi = -np.pi/2
        else:
            if(x> 0):
                phi = np.arctan (y/x)
            else:
                phi = np.arctan (y/x) + np.pi
    return r, theta, phi

class EditBlochSphereNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_EditBlochSphereNode"
    bl_label = "Edit Bloch Sphere"

    def create(self):
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0, minValue = 0)
        self.newInput("Vector", "Output State", "output_state")
        self.newInput("Object", "Bloch Sphere", "bloch_sphere")

    def execute(self, qubit_index,output_state,bloch_sphere ):
        if bloch_sphere is None:
            return
        try:
            bloch_data = _bloch_multivector_data(output_state)
            _theta = get_angles(bloch_data[qubit_index][0],bloch_data[qubit_index][1],bloch_data[qubit_index][2])[1]
            _phi = get_angles(bloch_data[qubit_index][0],bloch_data[qubit_index][1],bloch_data[qubit_index][2])[2]
            for i in range (len(bloch_sphere.children)):
                if (bloch_sphere.children[i].name == "Vector"):
                    vector = bloch_sphere.children[i]
            bpy.context.view_layer.objects.active = vector
            vector.select_set(True)
            vector.rotation_euler = (0.0, _theta, _phi)
        except:
            return