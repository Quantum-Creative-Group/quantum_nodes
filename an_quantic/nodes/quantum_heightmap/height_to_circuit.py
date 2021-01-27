import bpy
from ... lib.quantumblur import height2circuit
from animation_nodes.base_types import AnimationNode

class HeightmapToQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightmapToQuantumCircuitNode"
    bl_label = "Heightmap To Quantum Circuit"

    def create(self):
        self.newInput("Float List", "Floats", "floats")
        self.newOutput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")

    def execute(self, floats):
        if floats == []:
            return 0
        dictFloats = {}
        n = int(math.ceil(math.sqrt(len(floats))))
        iterator = 0
        for i in range(n):
            for j in range(n):
                if iterator < len(floats):
                    dictFloats[i,j] = float(format(abs(floats[iterator]), '.3f'))
                else:
                    dictFloats[i,j] = 0.0
                iterator += 1
        circuit = height2circuit(dictFloats)
        return circuit