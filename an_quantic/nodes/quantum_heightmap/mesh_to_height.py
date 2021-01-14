import bpy
import math # ceil, log
import numpy as np  # abs
from mathutils import Vector
from animation_nodes.base_types import AnimationNode

class MeshToHeight(bpy.types.Node, AnimationNode):
    bl_idname = "an_MeshToHeight"
    bl_label = "Mesh to Height"

    def create(self):
        self.newInput("Object", "Source", "source")
        self.newOutput("Vector List", "Negative Coordinates", "negativeCoord")
        self.newOutput("Vector List", "Heightmap", "heightmap")
        self.newOutput("Vector List", "Vertices", "vertices")

    def execute(self, source, index = 0):
        if source is None:
            return Vector((0, 0, 0)), Vector((0, 0, 0)), Vector((0, 0, 0))
        """ Converts a mesh into a python dictionnary containing one of 
        the (x, y, z) coordinates. Uses the exact same logic as James Wootton 
        about QuantumBlur for images, but applied on vertices of a mesh.
        """
        # vertices = source.data.vertices
        # source.data.vertices[0].co
        vertices = [ (source.matrix_world @ v.co) for v in source.data.vertices ]
        # verts = [vert.co for vert in bm.verts]
        # coords = [(obj.matrix_world @ v.co) for v in obj.data.vertices]
        # nb_vertices = len(vertices)
        nb_vertices = 8
        # negative_coords is used to get back negative values of coordinates (if there are)
        negative_coords, height = {}, {}
        # size of the dictionnary (n*n) corresponding to the mesh
        n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
        for i in range(n):
            for j in range(n):
                if (i+1)*(j+1) < nb_vertices:
                    # stores absolute value of vertex coord[index]
                    coord = vertices[(i+1)*(j+1)]   # .co[index]
                    height[i,j] = np.abs(coord)
                    if coord > 0: negative_coords[i,j] = 1.0
                    else: negative_coords[i,j] = -1.0
                else:
                    # if the vertex n°(i+1)*(j+1) does not exist
                    height[i,j] = 0.
                    negative_coords[i,j] = 1.0
                    
        return negative_coords, height, vertices