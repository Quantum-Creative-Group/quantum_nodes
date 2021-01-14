import bpy
from qiskit import *
from ... lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class QuantumCircuitToHeightmapNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitToHeightmapNode"
    bl_label = "Quantum Circuit To Heightmap"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newOutput("Vector List", "Heightmap", "heightmap")
        

    def execute(self, quantum_circuit):
        try:
            return circuit2height(quantum_circuit)
           
        except:
            return
        