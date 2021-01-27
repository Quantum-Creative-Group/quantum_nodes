import bpy
from ... lib.quantumblur import circuit2height
from animation_nodes.base_types import AnimationNode
from animation_nodes.data_structures import DoubleList

class QuantumCircuitToHeightmapNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitToHeightmapNode"
    bl_label = "Quantum Circuit To Heightmap"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "qc")
        self.newOutput("Float List", "Floats", "floats")
        
    def execute(self, qc):
        try:
            floats = DoubleList()
            dictFloats = {}
            dictFloats = circuit2height(qc)
            n = int(math.ceil(math.sqrt(len(dictFloats))))
            for i in range(n):
                for j in range(n):
                    floats.append(dictFloats[i,j])
            return floats
        except:
            return 