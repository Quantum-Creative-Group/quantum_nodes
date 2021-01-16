import bpy
from qiskit import *
from ... lib.quantumblur import *
from animation_nodes.base_types import AnimationNode

class HeightmapToQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightmapToQuantumCircuitNode"
    bl_label = "Heightmap To Quantum Circuit"

    def create(self):
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("Quantum Circuit", "Quantum Circuit 1", "quantum_circuit_1")
        self.newOutput("Quantum Circuit", "Quantum Circuit 2", "quantum_circuit_2")
        self.newOutput("Quantum Circuit", "Quantum Circuit 3", "quantum_circuit_3")

    def execute(self, heightmap):
        try:
            # heights = _image2heights(image)
            circuits = []
            for height in heights:
                circuits.append( height2circuit(height, log=log) )

            qc_1 = circuits[0]
            qc_2 = circuits[1]
            qc_3 = circuits[2]
            return qc_1, qc_2, qc_3
        except:
            return
        