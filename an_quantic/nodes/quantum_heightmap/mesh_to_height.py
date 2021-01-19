import bpy
import math # ceil, log
import numpy as np  # abs
from mathutils import Vector
from animation_nodes.data_structures import Vector3DList
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
        n = int(math.ceil(math.sqrt(nb_vertices)))    # the formulas seem to return the same result
        # n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
        heights = [{} for j in range(3)]
        negative_coords = [{} for j in range(3)]
        iterator = 0
        for i in range(n):
            for j in range(n):
                if iterator < nb_vertices:
                    xyz = coordinates[iterator]
                    for k in range(3):
                        heights[k][i,j] = float(format(abs(xyz[k]), '.3f'))
                        if xyz[k] >= 0: negative_coords[k][i,j] = 1.0
                        else: negative_coords[k][i,j] = -1.0
                else:
                    for k in range(3): heights[k][i,j] = 0.
                iterator += 1
    
        return heights, negative_coords

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newOutput("Vector 2D List", "Heightmap", "heightmap")
        self.newOutput("Vector 2D List", "Negative", "negative")
        self.newOutput("Float List", "Max Values", "max_values")
        self.newOutput("Vector List", "Vertices", "vertices")

    def execute(self, source):
        if source is None:
            return Vector((0, 0)), Vector((0,0)), Vector((0, 0, 0))
        """
        Converts a mesh into a python dictionnary containing one of 
        the (x, y, z) coordinates. Uses the exact same logic as James Wootton 
        about QuantumBlur for images, but applied on vertices of a mesh.
        """
        max_values = []
        vertices = Vector3DList.fromValues([ (v.co) for v in source.data.vertices ])
        heights, negative_coords = self.vertices2height(vertices)
        for height in heights:
            max_values.append(max(height.values()))
        return heights, negative_coords, max_values, vertices