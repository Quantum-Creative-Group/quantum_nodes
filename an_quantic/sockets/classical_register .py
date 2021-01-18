import bpy
from bpy.props import *
from qiskit import ClassicalRegister
from .. base_types import AnimationNodeSocket, PythonListSocket

class ClassicalRegisterSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_ClassicalRegisterSocket"
    bl_label = "Classical Register Socket"
    dataType = "Classical Register"
    drawColor = (0.73, 0.9, 0.768, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return ClassicalRegister(1)

#    @classmethod
#    def getCopyExpression(cls):
#        return "value.copy()"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, ClassicalRegister):
            return value, 0
        return cls.getDefaultValue(), 2

class ClassicalRegisterListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_ClassicalRegisterListSocket"
    bl_label = "ClassicalRegister List Socket"
    dataType = "ClassicalRegister List"
    baseType = ClassicalRegisterSocket
    drawColor = (0.18, 0.32, 1, 0.5)
    storable = True
    comparable = False

#    @classmethod
#    def getCopyExpression(cls):
#        return "[element.copy() for element in value]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, ClassicalRegister) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2
