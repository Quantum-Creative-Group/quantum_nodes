import bpy
import bmesh
import math
import numpy as np
import mathutils

def get_angles(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    if (r<10**-15):
        theta = 0
        phi = 0
    else :
        theta = np.arccos(z/r)
        if (x==0):
            if(y > 0):
                phi = np.pi/2
            else:
                phi = -np.pi/2
        else:
            if(x> 0):
                phi = np.arctan (y/x)
            else:
                phi = np.arctan (y/x) + np.pi
    return r, theta, phi
    
def creatFont(body, position_x, position_y, position_z, 
              rotation_x, rotation_y, rotation_z) :
    font = bpy.data.curves.new(type="FONT",name="Font Quantum Sphere "+body)
    font.body = body
    font_obj = bpy.data.objects.new("Font Object Quantum Sphere"+body, font)
    font_obj.rotation_euler = (rotation_x, rotation_y, rotation_z)
    font_obj.scale = (0.5,0.5,0.5)
    font_obj.location = (position_x , position_y, position_z)
    bpy.context.collection.objects.link(font_obj)
    bpy.context.view_layer.objects.active = font_obj
    font_obj.select_set(True)
    
def creatMesh(name, r, g, b, t):
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    material = bpy.data.materials.new("MyMaterial"+name)
    material.diffuse_color = (r, g, b, t)
    mesh.materials.append(material)
    
    bpy.context.collection.objects.link(object)
    bpy.context.view_layer.objects.active = object
    object.select_set(True)
    return mesh, object

def creatMultipleText(name, position_x, position_y, 
              rotation_x, rotation_y, rotation_z,size) :
    curves_left = {}
    text_objects_left = {}
    for i in range (11):
        curves_left["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT",name=name +str(i))
        curves_left["font_curve_{0}".format(i)].body = str(i/10)
        text_objects_left["font_obj_{0}".format(i)] = bpy.data.objects.new(name+str(i), curves_left["font_curve_{0}".format(i)])
        text_objects_left["font_obj_{0}".format(i)].rotation_euler = (rotation_x, rotation_y, rotation_z)
        text_objects_left["font_obj_{0}".format(i)].scale = (0.2,0.2,0.2)
        text_objects_left["font_obj_{0}".format(i)].location = (position_x,position_y,(size*i)/10 - 0.07)
        bpy.context.collection.objects.link(text_objects_left["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_left["font_obj_{0}".format(i)]
        text_objects_left["font_obj_{0}".format(i)].select_set(True)

def creatMultipleTextCity(my_name, position_x, position_y,
                                   rotation_x, rotation_y, rotation_z,size):
    curves_front = {}
    text_objects_front = {}
    for i in range (21):
        curves_front["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name= my_name +str(i))
        if (i<10) :
            curves_front["font_curve_{0}".format(i)].body = str(-(10-i)/10)
        else :
            curves_front["font_curve_{0}".format(i)].body = str((i-10)/10)
        text_objects_front["font_obj_{0}".format(i)] = bpy.data.objects.new(my_name + "Font Object"+str(i), curves_front["font_curve_{0}".format(i)])
        text_objects_front["font_obj_{0}".format(i)].rotation_euler = (rotation_x, rotation_y, rotation_z)
        text_objects_front["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_front["font_obj_{0}".format(i)].location = (position_x, position_y, (size*i)/10 - 0.07)
        bpy.context.collection.objects.link(text_objects_front["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_front["font_obj_{0}".format(i)]
        text_objects_front["font_obj_{0}".format(i)].select_set(True)

def historamCityDrawAxes(mesh, my_range, scale_x, scale_y, scale_z, 
                         translate1_x, translate1_y, translate1_z,
                         translate2_x, translate2_y, translate2_z) :
    bm = bmesh.new()
    for i in range (my_range) :
        if (i !=0) :
            bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((1/scale_x, 1/scale_y, 1/scale_z)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts = bm.verts, vec = mathutils.Vector((scale_x, scale_y, scale_z)))
        bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((translate1_x, translate1_y, translate1_z)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((translate2_x, translate2_y, translate2_z))) 
    bm.to_mesh(mesh)
    bm.free()