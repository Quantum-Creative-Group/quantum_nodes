import bpy
from qiskit import *
from .. lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class HeightmapToQuantumCircuit(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightmapToQuantumCircuittNode"
    bl_label = "Heightmap To Quantum Circuit"

    def create(self):
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("QuantumCircuit", "QuantumCircuit", "quantumCircuit")

    def execute(self, heightmap):
        try:
            quantumCircuit = height2circuit(heightmap)
            return quantumCircuit
        except:
            return
        