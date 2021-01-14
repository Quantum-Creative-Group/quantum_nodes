import bpy
from qiskit import *
from .. lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class QuantumCircuitToHeightmapNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitToHeightmapNode"
    bl_label = "Quantum Circuit To Heightmap"

    def create(self):
        self.newInput("QuantumCircuit", "QuantumCircuit", "quantumCircuit")
        self.newOutput("Vector List", "Heightmap", "heightmap")
        

    def execute(self, quantumCircuit):
        try:
            return circuit2height(quantumCircuit)
           
        except:
            return
        