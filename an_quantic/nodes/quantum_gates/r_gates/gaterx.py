import bpy
from qiskit import *
from math import pi
from animation_nodes.base_types import AnimationNode

class QuantumGateRXNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateRXNode"
    bl_label = "Quantum Gate RX"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Float", "Angle", "angle", value = pi)
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0, minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input ,qubit_index ,angle ):
     #   try:
        input.rx(angle,qubit_index)
        return input
     #   except:
      #      print ("didn't work")
      #      return