from bpy.types import NodeSocket
# from qiskit import QuantumCircuit
from qiskit_machine_learning.algorithms import QGAN
from animation_nodes.base_types import AnimationNodeSocket
import numpy as np


class QganSocket(NodeSocket, AnimationNodeSocket):
    """QGAN socket."""

    bl_idname = "an_QganSocket"
    bl_label = "qGAN Socket"
    dataType = "QGAN"
    drawColor = (0.29, 0.0, 0.5, 1.0)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return QGAN([1], np.array([1.0, 2.0]), [2], 1, 1, snapshot_dir=None)  # second to last 1 was 0.5

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, QGAN):
            return value, 0
        return cls.getDefaultValue(), 2
