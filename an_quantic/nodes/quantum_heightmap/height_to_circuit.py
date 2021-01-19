import bpy
from mathutils import Vector
from qiskit import *
from ... lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class HeightmapToQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightmapToQuantumCircuitNode"
    bl_label = "Heightmap To Quantum Circuit"

    def create(self):
        self.newInput("Vector 2D List", "Heightmap", "heightmap")
        self.newOutput("Quantum Circuit", "Quantum Circuit 1", "quantum_circuit_1")
        self.newOutput("Quantum Circuit", "Quantum Circuit 2", "quantum_circuit_2")
        self.newOutput("Quantum Circuit", "Quantum Circuit 3", "quantum_circuit_3")

    def execute(self, heightmap):
        if heightmap == {} or heightmap == Vector((0,0)):
            return {}, {}, {}
        # heights = _image2heights(image)
        circuits = []
        for height in heightmap:
            circuits.append( height2circuit(height) )

        qc_1 = circuits[0]
        qc_2 = circuits[1]
        qc_3 = circuits[2]
        return qc_1, qc_2, qc_3

        