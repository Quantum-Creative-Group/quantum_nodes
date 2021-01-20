import bpy
import math # ceil
import numpy as np  # sqrt
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList
from animation_nodes.base_types import AnimationNode

class HeighttoMesh(bpy.types.Node, AnimationNode):
    bl_idname = "an_HeightToMesh"
    bl_label = "Height to Mesh"

    def heights2mesh(self, vertices, negative_coords, heights, max_values):
        """
        [From James Wootton] Constructs an object from a set of vertices and three height dictionaries, one for each
        direction.
        """
        nb_vertices = len(vertices)
        n = int(math.ceil(np.sqrt(nb_vertices)))
        iterator = 0
        vertices = Vector3DList()

        for i in range(n):
            for j in range(n):
                xyz = Vector()
                for k, height in enumerate(heights):
                    if (i,j) in height and iterator < nb_vertices:
                        minus = negative_coords[k][i,j]
                        h = float(max_values[k]*height[i,j]) #we multiply again by the original max_value to inverse normalization
                    else:
                        h = 0
                    xyz[k] = float(minus*h)
                if iterator < nb_vertices:
                    vertices.append(xyz)
                iterator += 1
        return vertices

    def create(self):
        self.newInput("Object", "To modify", "modify")
        self.newInput("Vector 2D List", "Heightmap", "heightmap")
        self.newInput("Vector 2D List", "Negative Coordinates", "negativeCoord")
        self.newInput("Float List", "Max Values", "max_values")
        self.newOutput("Vector List", "Vertices", "vertices")

    def execute(self, modify, heightmap, negativeCoord, max_values):
        if negativeCoord == {} or heightmap == {} or modify is None:
            return {}
        """ Replaces the vertices by the new ones """
        vertices = [ (modify.matrix_world @ v.co) for v in modify.data.vertices ]
        vertices = self.heights2mesh(vertices, negativeCoord, heightmap, max_values)

        return vertices
