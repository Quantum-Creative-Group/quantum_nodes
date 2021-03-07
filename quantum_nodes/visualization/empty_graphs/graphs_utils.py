import bpy
import bmesh

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