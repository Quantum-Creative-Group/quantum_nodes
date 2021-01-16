import bpy
import math # ceil, log
import numpy as np  # abs
from mathutils import Vector
# from ... lib.quantumblur impor
from animation_nodes.base_types import AnimationNode

class MeshToHeight(bpy.types.Node, AnimationNode):
    bl_idname = "an_MeshToHeight"
    bl_label = "Mesh to Height"

    def vertices2height(self, coordinates):
        """
        [From James Wootton] Converts a vertices coordinates list into a list of three height dictionaries, one for
        each coordinates.
        """
        nb_vertices = len(coordinates)
        # n = int(math.ceil(math.sqrt(nb_vertices)))    # the formulas seem to return the same result
        n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
        heights = [{} for j in range(3)]
        negative_coords = [{} for j in range(3)]
        iterator = 0
        for i in range(n):
            for j in range(n):
                if iterator < nb_vertices:
                    xyz = coordinates[iterator]
                    for k in range(3):
                        heights[k][i,j] = abs(xyz[k])
                        if xyz[k] >= 0: negative_coords[k][i,j] = 1.0
                        else: negative_coords[k][i,j] = -1.0
                else:
                    for k in range(3): heights[k][i,j] = 0.
                iterator += 1

        return heights, negative_coords

    # def vertices2circuits(coordinates, log=False):
    #     """
    #     Converts an image to a set of three circuits, with one corresponding to
    #     each RGB colour channel.

    #     Args:
    #         coordinates (Vector List): A list of the vertices' coordinates.
    #         log (bool): If given, a logarithmic encoding is used.

    #     Returns:
    #         circuits (list): A list of quantum circuits encoding the vertices.
    #     """

    #     heights = vertices2height(coordinates)

    #     circuits = []
    #     for height in heights:
    #         circuits.append( height2circuit(height, log=log) )

    #     return circuits

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newOutput("Vector 2D List", "Heightmap", "heightmap")
        self.newOutput("Vector 2D List", "Negative", "negative")
        self.newOutput("Vector List", "Vertices", "vertices")

    def execute(self, source):
        if source is None:
            return Vector((0, 0)), None, Vector((0, 0, 0))
        """
        Converts a mesh into a python dictionnary containing one of 
        the (x, y, z) coordinates. Uses the exact same logic as James Wootton 
        about QuantumBlur for images, but applied on vertices of a mesh.
        """
        vertices = [ (source.matrix_world @ v.co) for v in source.data.vertices ]
        heights, negative_coords = self.vertices2height(vertices)
        # circuits = vertices2circuits(vertices)
        offset = len(vertices)
            
        return heights, negative_coords, vertices