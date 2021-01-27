import bpy
from qiskit.result.counts import Counts
from animation_nodes.base_types import AnimationNodeSocket, PythonListSocket

class QuantumCountSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_QuantumCountSocket"
    bl_label = "Quantum Count Socket"
    dataType = "Quantum Count"
    drawColor = (0.73, 0.9, 0.768, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

#    @classmethod
#    def getCopyExpression(cls):
#        return "value.copy()"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, qiskit.result.counts.Counts):
            return value, 0
        return cls.getDefaultValue(), 2

class QuantumCountListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_QuantumCountListSocket"
    bl_label = "Quantum Count List Socket"
    dataType = "Quantum Count List"
    baseType = QuantumCountSocket
    drawColor = (0.18, 0.32, 1, 0.5)
    storable = True
    comparable = False

#    @classmethod
#    def getCopyExpression(cls):
#        return "[element.copy() for element in value]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, qiskit.result.counts.Counts) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2
