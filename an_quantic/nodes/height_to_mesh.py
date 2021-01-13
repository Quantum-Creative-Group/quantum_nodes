import bpy
from animation_nodes.base_types import AnimationNode

class HeighttoMesh(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightToMesh"
    bl_label = "Height to Mesh"

    def create(self):
        self.newInput("Vector List", "Negative Coordinates", "negativeCoord")
        self.newInput("Vector List", "Heightmap", "heightmap")
        self.newOutput("Object", "Result", "result")

    def execute(self, source, index = 0):
        if source is None:
            return
        """ Replaces the vertices by the new ones """
        nb_vertices = len(vertices)
        n = int(np.sqrt(len(height)))
        for i in range(n):
            for j in range(n):
                if (i+1)*(j+1) < nb_vertices:
                    coord = height[i,j] * negative_coords[i,j] + distance
                    vertices[(i+1)*(j+1)].co[index] = coord
