import bpy
import bmesh
from math import radians
from mathutils import (Matrix, Vector)
from numpy import pi
from .. utils.graphs_utils import creatFont, creatMesh
    
def plotEmptyBlochSphere():   
    bpy.ops.object.select_all(action='DESELECT') #deselect all object

    #Sphere-------------------------------------------------------------
    mesh_sphere, sphere = creatMesh("QuantumBlochSphere", 0.37, 0.59, 0.9, 0.1)   

    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments = 32, v_segments = 16, diameter = 2)
    bm.to_mesh(mesh_sphere)
    bm.free()
    bpy.ops.object.modifier_add(type = 'SUBSURF')
    bpy.ops.object.shade_smooth()
    #--------------------------------------------------------------------

    #Axes-------------------------------------------------------------
    mesh_axes, axes = creatMesh("QuantumBlochAxes", 1., 1., 1., 1.)   

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=Matrix.Rotation(radians(90.0), 3, 'X'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=Matrix.Rotation(radians(90.0), 3, 'Y'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bm.to_mesh(mesh_axes)
    bm.free()
    #--------------------------------------------------------------------

    #Light_Axes-------------------------------------------------------------
    mesh_light_axes, light_axes = creatMesh("QuantumBlochLightAxes", 0.2, 0.2, 0.2, 1.)  

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.915, diameter2=1.915, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.915, diameter2=1.915, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, -0.5)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, -1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.71, diameter2=1.71, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.71, diameter2=1.71, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, -1.)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, -1.5)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.29, diameter2=1.29, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.5)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.5)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.29, diameter2=1.29, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, -1.5)))
    bm.to_mesh(mesh_light_axes)
    bm.free()

    mesh_light_axes_2, light_axes_2 = creatMesh("QuantumBlochLightAxes2", 0.2, 0.2, 0.2, 1.)  

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=Matrix.Rotation(radians(90.0), 3, 'Y'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=Matrix.Rotation(radians(45.0), 3, 'Y'))
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=Matrix.Rotation(radians(90.0), 3, 'X'))
    bm.to_mesh(mesh_light_axes_2)
    bm.free()
    #--------------------------------------------------------------------

    #Vector-------------------------------------------------------------
    mesh_vector, vector = creatMesh("QuantumBlochVector", 0.73, 0.04, 0.04, 1.)  

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=20, diameter1=0.1, diameter2=0., depth=0.2)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=20, diameter1=0.05, diameter2=0.05, depth=1.9)
    bmesh.ops.translate(bm, verts = bm.verts, vec = Vector((0.0, 0.0, 0.95)))
    bm.to_mesh(mesh_vector)
    bm.free()
    #--------------------------------------------------------------------
    
    #Text
    ##################################################################################
    creatFont("quibit", 0.4, -0.4, 3., pi/2, 0, pi*(3/4))
    creatFont("|0>", 0.2, -0.2, 2.3, pi/2, 0, pi*(3/4))
    creatFont("|1>", 0.2, -0.2, -2.5, pi/2, 0, pi*(3/4))
    creatFont("x", 2.1, 0., 0., pi/2,0,0)
    creatFont("y", 0. , 2.1, 0.,pi/2,0,pi/2)
    ##################################################################################
    
    #Join all objects
    vector.select_set(False)
    bpy.context.view_layer.objects.active = sphere 
    bpy.ops.object.join()
    vector.select_set(True)
    bpy.ops.object.parent_set()