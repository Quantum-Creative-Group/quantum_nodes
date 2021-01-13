import bpy
import numpy as np  # sqrt
from animation_nodes.base_types import AnimationNode

class HeighttoMesh(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightToMesh"
    bl_label = "Height to Mesh"

    def create(self):
        self.newInput("Object", "To modify", "modify")
        self.newInput("Vector List", "Negative Coordinates", "negativeCoord")
        self.newInput("Vector List", "Heightmap", "heightmap")

    def execute(self, modify, negativeCoord, heightmap, index = 0):
        if negativeCoord is None or heightmap is None or modify is None:
            return
        """ Replaces the vertices by the new ones """
        vertices = modify.data.vertices[:]
        nb_vertices = len(vertices)
        n = int(np.sqrt(len(heightmap)))
        for i in range(n):
            for j in range(n):
                if (i+1)*(j+1) < nb_vertices:
                    coord = heightmap[i,j] * negativeCoord[i,j]
                    vertices[(i+1)*(j+1)].co[index] = coord
