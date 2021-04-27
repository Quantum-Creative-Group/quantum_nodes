import bpy
import bmesh
import mathutils
import numpy as np
from qiskit import *
from qiskit.visualization.utils import _bloch_multivector_data
from ..empty_graphs.plotEmptyHistogram import plotHistogram

def editHistogram(parent, _counts, _shots):
    #data
    keys = list(_counts)
    nb_cubes = len(keys)
    X = 3.2
    Y = 0.7
    Z = nb_cubes
    T = 0.01
    H = 0.25
    size = 3
    
    bpy.ops.object.select_all(action='DESELECT') #deselect all object

    #Cubes-------------------------------------------------------------
    mesh_cube = bpy.data.meshes.new('Cube')
    cube = bpy.data.objects.new("Cube", mesh_cube)
    material_cube = bpy.data.materials.new("MyMaterialCube")
    material_cube.diffuse_color = (0., 0., 1., 0.9)
    mesh_cube.materials.append(material_cube)
    
    bpy.context.collection.objects.link(cube)
    bpy.context.view_layer.objects.active = cube
    cube.select_set(True)

    bm = bmesh.new()
    for i in range (nb_cubes) :
        scale = _counts[keys[i]]/_shots
        resize = 0.5/(scale*size)
        if (i != 0):
            bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 1.0, 0.0)))
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/resize, 1/resize, 1)))
            bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, (-scale*size)/2)))
        bmesh.ops.create_cube(bm, size=scale*size)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((resize, resize, 1.)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, (scale*size)/2)))   
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.5, 0.0))) 
    bm.to_mesh(mesh_cube)
    bm.free()
    #--------------------------------------------------------------------

    plotHistogram(nb_cubes, X, Y, Z, T, H, size)
        
    curves_results_probabilities = {}
    text_objects_results_probabilities = {}
    for i in range (nb_cubes):
        probability = _counts[keys[i]]/_shots
        curves_results_probabilities["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        curves_results_probabilities["font_curve_{0}".format(i)].body = str(probability)
        text_objects_results_probabilities["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_results_probabilities["font_curve_{0}".format(i)])
        text_objects_results_probabilities["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,-np.pi/2,np.pi/2)
        text_objects_results_probabilities["font_obj_{0}".format(i)].scale = (0.2,0.2,0.2)
        text_objects_results_probabilities["font_obj_{0}".format(i)].location = (0.05,(nb_cubes-i)-0.4, probability*size + 0.2)
        bpy.context.collection.objects.link(text_objects_results_probabilities["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_results_probabilities["font_obj_{0}".format(i)]
        text_objects_results_probabilities["font_obj_{0}".format(i)].select_set(True)
        
    curves_results = {}
    text_objects_results = {}
    for i in range (nb_cubes):
        curves_results["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        curves_results["font_curve_{0}".format(i)].body = keys[i]
        text_objects_results["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_results["font_curve_{0}".format(i)])
        text_objects_results["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,-np.pi,-np.pi/2)
        text_objects_results["font_obj_{0}".format(i)].scale = (0.2,0.2,0.2)
        text_objects_results["font_obj_{0}".format(i)].location = (Y+0.01,(nb_cubes-i)-0.7, 0.0)
        bpy.context.collection.objects.link(text_objects_results["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_results["font_obj_{0}".format(i)]
        text_objects_results["font_obj_{0}".format(i)].select_set(True)

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
    faces.select_set(True)