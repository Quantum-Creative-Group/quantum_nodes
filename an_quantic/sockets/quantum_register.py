import bpy
from bpy.props import *
from qiskit import QuantumRegister
from animation_nodes.base_types import AnimationNodeSocket, PythonListSocket

class QuantumRegisterSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_QuantumRegisterSocket"
    bl_label = "Quantum Register Socket"
    dataType = "Quantum Register"
    drawColor = (1.0, 0.16, 0.0, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return QuantumRegister(1)

#    @classmethod
#    def getCopyExpression(cls):
#        return "value.copy()"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, QuantumRegister):
            return value, 0
        return cls.getDefaultValue(), 2


class QuantumRegisterListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_QuantumRegisterListSocket"
    bl_label = "Quantum Register List Socket"
    dataType = "Quantum Register List"
    baseType = QuantumRegisterSocket
    drawColor = (0.18, 0.32, 1, 0.5)
    storable = True
    comparable = False

#    @classmethod
#    def getCopyExpression(cls):
#        return "[element.copy() for element in value]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, QuantumRegister) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2