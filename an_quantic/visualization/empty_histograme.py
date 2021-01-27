import bpy
import bmesh
import mathutils
import math
import numpy as np
from qiskit import *
from qiskit.visualization.utils import _bloch_multivector_data

def plot_histograme(): 
    #data
    nb_cubes = 2
    X = 3.2
    Y = 0.7
    Z = nb_cubes
    T = 0.01
    H = 0.25
    size = 3
    
    bpy.ops.object.select_all(action='DESELECT') #deselect all object
    
    mesh_parent = bpy.data.meshes.new('Parent')
    parent = bpy.data.objects.new("Parent", mesh_parent)
    material_parent = bpy.data.materials.new("MyMaterialParent")
    material_parent.diffuse_color = (1., 1., 1., 0.)
    mesh_parent.materials.append(material_parent)
    
    bpy.context.collection.objects.link(parent)
    bpy.context.view_layer.objects.active = parent
    parent.select_set(True)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bm.to_mesh(mesh_parent)
    bm.free()

    #Faces-------------------------------------------------------------
    mesh_faces = bpy.data.meshes.new('Quantume_Faces')
    faces = bpy.data.objects.new("Quantume_Faces", mesh_faces)
    material_faces = bpy.data.materials.new("MyMaterialFaces")
    material_faces.diffuse_color = (1., 1., 1., 1.)
    mesh_faces.materials.append(material_faces)
    
    bpy.context.collection.objects.link(faces)
    bpy.context.view_layer.objects.active = faces
    faces.select_set(True)
    
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
    mesh_axes_front = bpy.data.meshes.new('AxesFront')
    axes_front = bpy.data.objects.new("AxesFront", mesh_axes_front)
    mesh_axes_left = bpy.data.meshes.new('AxesLeft')
    axes_left = bpy.data.objects.new("AxesLeft", mesh_axes_left)
    material_axes = bpy.data.materials.new("MyMaterialAxes")
    material_axes.diffuse_color = (0., 0., 0., 1.)
    mesh_axes_front.materials.append(material_axes)
    mesh_axes_left.materials.append(material_axes)
    
    bpy.context.collection.objects.link(axes_front)
    bpy.context.view_layer.objects.active = axes_front
    axes_front.select_set(True)

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
    
    bpy.context.collection.objects.link(axes_left)
    bpy.context.view_layer.objects.active = axes_left
    axes_left.select_set(True)
    
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
    
    #Text
    curves_front = {}
    text_objects_front = {}
    for i in range (11):
        curves_front["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        curves_front["font_curve_{0}".format(i)].body = str(i/10)
        text_objects_front["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_front["font_curve_{0}".format(i)])
        text_objects_front["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,0,np.pi/2)
        text_objects_front["font_obj_{0}".format(i)].scale = (0.2,0.2,0.2)
        text_objects_front["font_obj_{0}".format(i)].location = (-0.25,nb_cubes+0.1 ,(size*i)/10 - 0.07)
        bpy.context.collection.objects.link(text_objects_front["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_front["font_obj_{0}".format(i)]
        text_objects_front["font_obj_{0}".format(i)].select_set(True)
        
    curves_left = {}
    text_objects_left = {}
    for i in range (11):
        curves_left["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        curves_left["font_curve_{0}".format(i)].body = str(i/10)
        text_objects_left["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_left["font_curve_{0}".format(i)])
        text_objects_left["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,0,np.pi)
        text_objects_left["font_obj_{0}".format(i)].scale = (0.2,0.2,0.2)
        text_objects_left["font_obj_{0}".format(i)].location = (Y+0.1,0.0,(size*i)/10 - 0.07)
        bpy.context.collection.objects.link(text_objects_left["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_left["font_obj_{0}".format(i)]
        text_objects_left["font_obj_{0}".format(i)].select_set(True)
        
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