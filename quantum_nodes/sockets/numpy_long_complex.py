from bpy.types import NodeSocket
from numpy import complex128, ndarray
from animation_nodes.data_structures import LongList
from animation_nodes.base_types import AnimationNodeSocket, PythonListSocket


class Complex128Socket(NodeSocket, AnimationNodeSocket):
    """Numpy complex 128 socket."""

    bl_idname = "an_Complex128Socket"
    bl_label = "Complex128 Socket"
    dataType = "Complex128"
    drawColor = (0.6, 0.95, 0.25, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return complex128(0. + 0. * 1j)

    @classmethod
    def correctValue(cls, value):

        if isinstance(value, complex128):
            return value, 0
        return cls.getDefaultValue(), 2


class Complex128ListSocket(NodeSocket, PythonListSocket):
    """List of numpy complex 128 socket."""

    bl_idname = "an_Complex128ListSocket"
    bl_label = "Complex128 List Socket"
    dataType = "Complex128 List"
    baseType = Complex128Socket
    drawColor = (0.6, 0.95, 0.25, 0.5)
    storable = True
    comparable = False

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list) or isinstance(value, ndarray):
            if all(isinstance(element, complex128) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2
