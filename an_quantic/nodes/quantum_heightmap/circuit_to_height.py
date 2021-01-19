import bpy
from qiskit import *
from ... lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class QuantumCircuitToHeightmapNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitToHeightmapNode"
    bl_label = "Quantum Circuit To Heightmap"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit 1", "qc_1")
        self.newInput("Quantum Circuit", "Quantum Circuit 2", "qc_2")
        self.newInput("Quantum Circuit", "Quantum Circuit 3", "qc_3")
        self.newOutput("Vector 2D List", "Heightmap", "heightmap")
        

    def execute(self, qc_1, qc_2, qc_3):
        try:
            heights = []
            heights.append( circuit2height(qc_1) )
            heights.append( circuit2height(qc_2) )
            heights.append( circuit2height(qc_3) )
            
            return heights
        except:
            return