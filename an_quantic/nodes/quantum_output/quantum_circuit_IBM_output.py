import bpy
# from qiskit import *
from qiskit import IBMQ
from animation_nodes.base_types import AnimationNode

# import re
from bpy.props import * # ...Property
# from animation_nodes.utils.code import isCodeValid
# from animation_nodes.utils.layout import splitAlignment
from animation_nodes.events import executionCodeChanged
# from animation_nodes.execution.code_generator import iter_Imports

from animation_nodes.nodes.spline.c_utils import getMatricesAlongSpline
from animation_nodes.data_structures import Mesh, LongList
from animation_nodes.nodes.mesh.c_utils import getReplicatedVertices
from animation_nodes.nodes.spline.spline_evaluation_base import SplineEvaluationBase
from animation_nodes.algorithms.mesh_generation.circle import getPointsOnCircle
from animation_nodes.algorithms.mesh_generation.grid import quadEdges, quadPolygons

class QuantumCircuitOutputStateNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitIBMOutputStateNode"
    bl_label = "Quantum Circuit IBM Output State"

    token: StringProperty(name = "Token",
        description = "Copy your IBM quantum experience token here",
        update = executionCodeChanged)

    def create(self):
        self.newInput("Spline", "Spline", "spline", defaultDrawType = "PROPERTY_ONLY")

    def drawAdvanced(self, layout):
        layout.prop(self, "token")
        col = layout.column()

        # col.prop(self, "parameterType")
        # subcol = col.column()
        # subcol.active = self.parameterType == "UNIFORM"
        # subcol.prop(self, "resolution")

    