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