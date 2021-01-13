import bpy
import sys
from bpy.props import *
from mathutils import Vector
from animation_nodes.events import propertyChanged
from animation_nodes.base_types import AnimationNodeSocket, CListSocket
from animation_nodes.utils.attributes import getattrRecursive
from animation_nodes.sockets.info import toIdName as toSocketIdName

class QuantumSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_QuantumSocket"
    bl_label = "Quantum Socket"
    dataType = "Quantum"
    drawColor = (0.7, 0.7, 0.4, 1)
    storable = True
    comparable = True

    value: FloatVectorProperty(default = [0, 0, 0], update = propertyChanged, subtype = "XYZ")

    def drawProperty(self, layout, text, node):
        col = layout.column(align = True)
        if text != "": col.label(text = text)
        col.prop(self, "value", index = 0, text = "X")
        col.prop(self, "value", index = 1, text = "Y")
        col.prop(self, "value", index = 2, text = "Z")

    def getValue(self):
        return Vector(self.value)

    def setProperty(self, data):
        self.value = data

    def getProperty(self):
        return self.value[:]

    @classmethod
    def getDefaultValue(cls):
        return Vector((1, 1, 1))

    @classmethod
    def getCopyExpression(cls):
        return "value.copy()"

