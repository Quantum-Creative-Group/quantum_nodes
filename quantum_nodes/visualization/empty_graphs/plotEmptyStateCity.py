import bpy
import bmesh
import mathutils
import math
import numpy as np
from qiskit import *
from qiskit.quantum_info.states import DensityMatrix

def plotEmptyStateCity():      
    # data
    nb_cubes = 4
    
    # dimensions
    #                 Z
    #         + + + + + + + + +
    #    Y  + -               +
    #     +   -               + 
    #   +     -               +       
    #   +     - - - - - - - - +   
    # X +   -               +
    #   + -               +
    #   + + + + + + + + +
    
    size = 3
    X = size*2
    Y = nb_cubes + 0.5
    Z = nb_cubes + 0.5
    T = 0.01
    H = 0.25

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
    mesh_faces = bpy.data.meshes.new('Quantume_City_Faces')
    faces = bpy.data.objects.new("Quantume_City_Faces", mesh_faces)
    material_faces = bpy.data.materials.new("MyMaterialFaces")
    material_faces.diffuse_color = (1., 1., 1., 1.)
    mesh_faces.materials.append(material_faces)
    
    bpy.context.collection.objects.link(faces)
    bpy.context.view_layer.objects.active = faces
    faces.select_set(True)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T, Z, X)))  
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y+0.5, Z/2, X/2)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector(((Y-1.)/2, 0.0, -X/2)))
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y, 1/T, 1/X))) 
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y, T, X))) 
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-(Y-1.)/2, 0.0, X/2)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector(((Y-1.)/2, -Z/2, 0.0)))
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y, 1/Z, 1/T))) 
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y, Z, T))) 
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-(Y-1.)/2, Z/2, 0.0)))
    bm.to_mesh(mesh_faces)
    bm.free()
    
    mesh_transparent_face = bpy.data.meshes.new('TransparentFaces')
    transparent_face = bpy.data.objects.new("TransparentFaces", mesh_transparent_face)
    material_transparent_face = bpy.data.materials.new("MyMaterialTransparentFace")
    material_transparent_face.diffuse_color = (1., 1., 1., 0.1)
    mesh_transparent_face.materials.append(material_transparent_face)
    
    bpy.context.collection.objects.link(transparent_face)
    bpy.context.view_layer.objects.active = transparent_face
    transparent_face.select_set(True)
    
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y, Z, T)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-(Y-1.)/2, Z/2, size)))
    bm.to_mesh(mesh_transparent_face)
    bm.free()
    #--------------------------------------------------------------------
    
    #Axes-------------------------------------------------------------
    mesh_axes_front = bpy.data.meshes.new('AxesFront')
    axes_front = bpy.data.objects.new("AxesFront", mesh_axes_front)
    mesh_axes_left = bpy.data.meshes.new('AxesLeft')
    axes_left = bpy.data.objects.new("AxesLeft", mesh_axes_left)
    mesh_axes_vertical_front = bpy.data.meshes.new('AxesFront')
    axes_vertical_front = bpy.data.objects.new("AxesFront", mesh_axes_vertical_front)
    mesh_axes_vertical_left = bpy.data.meshes.new('AxesFront')
    axes_vertical_left = bpy.data.objects.new("AxesFront", mesh_axes_vertical_left)
    
    mesh_axes_bottom_vertical = bpy.data.meshes.new('AxesFront')
    axes_bottom_vertical = bpy.data.objects.new("AxesFront", mesh_axes_bottom_vertical)
    mesh_axes_bottom_horizontal = bpy.data.meshes.new('AxesFront')
    axes_bottom_horizontal = bpy.data.objects.new("AxesFront", mesh_axes_bottom_horizontal)
    
    material_axes = bpy.data.materials.new("MyMaterialAxes")
    material_axes.diffuse_color = (0., 0., 0., 1.)
    mesh_axes_front.materials.append(material_axes)
    mesh_axes_left.materials.append(material_axes)
    mesh_axes_vertical_front.materials.append(material_axes)
    mesh_axes_vertical_left.materials.append(material_axes)
    mesh_axes_bottom_vertical.materials.append(material_axes)
    mesh_axes_bottom_horizontal.materials.append(material_axes)
    
    bpy.context.collection.objects.link(axes_front)
    bpy.context.view_layer.objects.active = axes_front
    axes_front.select_set(True)

    bm = bmesh.new()
    for i in range (19) :
        if (i !=0) :
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/T,1/Y , 1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T,Y , T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, size/10)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y+0.51, Y/2, 0.0))) 
    bm.to_mesh(mesh_axes_front)
    bm.free()
    
    bpy.context.collection.objects.link(axes_left)
    bpy.context.view_layer.objects.active = axes_left
    axes_left.select_set(True)
    
    bm = bmesh.new()
    for i in range (19):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y,1/T,1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y,T,T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0,size/10)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-(Y-1.)/2,T, 0.0))) 
    bm.to_mesh(mesh_axes_left)
    bm.free()
    
    bpy.context.collection.objects.link(axes_vertical_front)
    bpy.context.view_layer.objects.active = axes_vertical_front
    axes_vertical_front.select_set(True)
    
    bm = bmesh.new()
    for i in range (nb_cubes):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/T,1/T,1/X)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T,T,X)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0,(Y-0.5)/nb_cubes, 0.0)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y+0.51,-0.5, X/2))) 
    bm.to_mesh(mesh_axes_vertical_front)
    bm.free()
    
    bpy.context.collection.objects.link(axes_vertical_left)
    bpy.context.view_layer.objects.active = axes_vertical_left
    axes_vertical_left.select_set(True)
    
    bm = bmesh.new()
    for i in range (nb_cubes):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/T,1/T,1/X)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T,T,X)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector(((Y-0.5)/nb_cubes,0.0,0.0)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y,T, X/2))) 
    bm.to_mesh(mesh_axes_vertical_left)
    bm.free()
    
    bpy.context.collection.objects.link(axes_bottom_vertical)
    bpy.context.view_layer.objects.active = axes_bottom_vertical
    axes_bottom_vertical.select_set(True)
    
    bm = bmesh.new()
    for i in range (nb_cubes):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/Y,1/T,1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((Y,T,T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0,(Y-0.5)/nb_cubes,0.0)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y/2+0.5,-0.5, T))) 
    bm.to_mesh(mesh_axes_bottom_vertical)
    bm.free()
    
    bpy.context.collection.objects.link(axes_bottom_horizontal)
    bpy.context.view_layer.objects.active = axes_bottom_horizontal
    axes_bottom_horizontal.select_set(True)
    
    bm = bmesh.new()
    for i in range (nb_cubes):
        if (i !=0):
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/T,1/Y,1/T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((T,Y,T)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector(((Y-0.5)/nb_cubes, 0.0,0.0)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((-Y,Z/2, T))) 
    bm.to_mesh(mesh_axes_bottom_horizontal)
    bm.free()
    
    #--------------------------------------------------------------------
    
    #Text
    curves_front = {}
    text_objects_front = {}
    for i in range (21):
        curves_front["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        if (i<10) :
            curves_front["font_curve_{0}".format(i)].body = str(-(10-i)/10)
        else :
            curves_front["font_curve_{0}".format(i)].body = str((i-10)/10)
        text_objects_front["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_front["font_curve_{0}".format(i)])
        text_objects_front["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,0,np.pi/2)
        text_objects_front["font_obj_{0}".format(i)].scale = (0.3,0.3,0.3)
        text_objects_front["font_obj_{0}".format(i)].location = (-Y+0.5,Y+0.1 ,(size*i)/10 - 0.07)
        bpy.context.collection.objects.link(text_objects_front["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_front["font_obj_{0}".format(i)]
        text_objects_front["font_obj_{0}".format(i)].select_set(True)
        
    curves_left = {}
    text_objects_left = {}
    for i in range (21):
        curves_left["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name="Font Curve" +str(i))
        if (i<10) :
            curves_left["font_curve_{0}".format(i)].body = str(-(10-i)/10)
        else :
            curves_left["font_curve_{0}".format(i)].body = str((i-10)/10)
        text_objects_left["font_obj_{0}".format(i)] = bpy.data.objects.new("Font Object"+str(i), curves_left["font_curve_{0}".format(i)])
        text_objects_left["font_obj_{0}".format(i)].rotation_euler = (np.pi/2,0,np.pi)
        text_objects_left["font_obj_{0}".format(i)].scale = (0.3,0.3,0.3)
        text_objects_left["font_obj_{0}".format(i)].location = (1.,0.0,(size*i)/10 - 0.07)
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
