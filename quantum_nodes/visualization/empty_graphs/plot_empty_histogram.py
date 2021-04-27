import bpy
import bmesh
import mathutils
import math
import numpy as np
from qiskit.visualization.utils import _bloch_multivector_data
from .. utils.graphs_utils import creatMultipleText, creatMesh

    
def plotEmptyHistogram(): 
    #data
    nb_cubes = 2
    X = 3.2
    Y = 0.7
    Z = nb_cubes
    T = 0.01
    H = 0.25
    size = 3

    bpy.ops.object.select_all(action='DESELECT') #deselect all objects 
    mesh_parent, parent = creatMesh("QuantumHistogramParent", 1., 1., 1., 0.)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bm.to_mesh(mesh_parent)
    bm.free()

    #Faces-------------------------------------------------------------
    mesh_faces, faces = creatMesh("QuantumHistogramFaces", 1., 1., 1., 1.)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T, Z, X)))  
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-H, Z/2, X/2)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-0.1, 0.0, -X/2)))
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y, 1/T, 1/X))) 
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y, T, X))) 
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.1, 0.0, X/2)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-0.1, -Z/2, 0.0)))
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y, 1/Z, 1/T))) 
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y, Z, T))) 
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.1, Z/2, 0.0)))
    bm.to_mesh(mesh_faces)
    bm.free()
    #--------------------------------------------------------------------
    
    #Axes-------------------------------------------------------------
    mesh_axes_front, axes_front = creatMesh("QuantumHistogramAxesFront", 0., 0., 0., 1.)  

    bm = bmesh.new()
    for i in range (10) :
        if (i !=0) :
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/T,1/nb_cubes , 1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T,nb_cubes , T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, size/10)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-(H-T), nb_cubes/2, 0.0))) 
    bm.to_mesh(mesh_axes_front)
    bm.free()
    
    mesh_axes_left, axes_left = creatMesh("QuantumHistogramAxesFront", 0., 0., 0., 1.)
    
    bm = bmesh.new()
    for i in range (10):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y,1/T,1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y,T,T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0,size/10)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.1,T, 0.0))) 
    bm.to_mesh(mesh_axes_left)
    bm.free()
    #--------------------------------------------------------------------
    
    #Text------------------------------------------------------------------    
    creatMultipleText("QuantumHistogramFontRight", -0.25,nb_cubes+0.1, np.pi/2,0,np.pi/2,size)
    creatMultipleText("QuantumHistogramFontLeft", Y+0.1,0.0, np.pi/2,0,np.pi,size)
    #---------------------------------------------------------------------
        
    parent.select_set(False)
    bpy.context.view_layer.objects.active = faces 
    bpy.ops.object.join()
    bpy.ops.object.parent_set()
    
    bpy.ops.object.select_all(action='DESELECT')
    parent.select_set(True)
    faces.select_set(True)
    bpy.context.view_layer.objects.active = parent 
    bpy.ops.object.parent_set() 
    parent.select_set(False)



