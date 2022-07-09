from bpy.types import NodeSocket

from qiskit.result.counts import Counts
from animation_nodes.base_types import AnimationNodeSocket, PythonListSocket


class QuantumCountSocket(NodeSocket, AnimationNodeSocket):
    """Quantum count socket."""

    bl_idname = "an_QuantumCountSocket"
    bl_label = "Quantum Count Socket"
    dataType = "Quantum Count"
    drawColor = (0.73, 0.9, 0.768, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return None

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, Counts):
            return value, 0
        return cls.getDefaultValue(), 2


class QuantumCountListSocket(NodeSocket, PythonListSocket):
    """List of quantum counts socket."""

    bl_idname = "an_QuantumCountListSocket"
    bl_label = "Quantum Count List Socket"
    dataType = "Quantum Count List"
    baseType = QuantumCountSocket
    drawColor = (0.18, 0.32, 1, 0.5)
    storable = True
    comparable = False

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, Counts) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2
