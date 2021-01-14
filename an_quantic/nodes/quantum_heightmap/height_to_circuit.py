import bpy
from qiskit import *
from ... lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class HeightmapToQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightmapToQuantumCircuitNode"
    bl_label = "Heightmap To Quantum Circuit"

    def create(self):
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("QuantumCircuit", "QuantumCircuit", "quantumCircuit")

    def execute(self, heightmap):
        try:
            return height2circuit(heightmap)
        except:
            return
        