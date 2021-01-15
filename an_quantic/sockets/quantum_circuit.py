import bpy
from bpy.props import *
from qiskit import QuantumCircuit
from .. base_types import AnimationNodeSocket

class QuantumCircuitSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_QuantumCircuitSocket"
    bl_label = "Quantum Circuit Socket"
    dataType = "Quantum Circuit"
    drawColor = (0.29, 0.0, 0.5, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return QuantumCircuit(1)

#    @classmethod
#    def getCopyExpression(cls):
#        return "value.copy()"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, QuantumCircuit):
            return value, 0
        return cls.getDefaultValue(), 2

  
