import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode
import bmesh
import mathutils
import math
import numpy as np
from qiskit.visualization.utils import _bloch_multivector_data

def get_bloch_sphere_angles(_alpha, _beta):
    #input = two complexe numbers alpha and beta wich represent the state of the qubit
    #alpha = a +i b, beta = c + i d
    a = _alpha.real
    b = _alpha.imag
    c = _beta.real
    d = _beta.imag
    
    if(a==0 and b == 0 and c == 0 and d == 0):
        theta = 0
        phi = 0
    if (b==0):
        theta = 2*np.arccos(a)
        if(c == 0 and d == 0):
            phi = 0
        elif(c == 0):
            if(d>0):
                phi = np.pi/2
            else:
                phi = -np.pi/2
        else:
            if (c > 0):
                phi = np.arctan(d/c)
            else:
                phi = np.arctan(d/c) + np.pi
    else: 
        theta = 2*np.arccos(abs(_alpha)) 
        if (a==0):
            if(b > 0):
                global_phase = np.pi/2
            else:
                global_phase = -np.pi/2
        else:
            if(a> 0):
                global_phase = np.arctan (b/a)
            else:
                global_phase = np.arctan (b/a) + np.pi

        B = (d*np.cos(global_phase)-c*np.sin(global_phase))
        A = (c*np.cos(global_phase)+d*np.sin(global_phase))
        if (A==0):
            if(B==0):
                phi = np.pi/2
            else:
                phi = -np.pi/2
        else:
            if(A>0):
                phi = np.arctan(B/A)
            else:
                phi = np.arctan(B/A) + np.pi
    return theta, phi 


def bloch_sphere(_alpha, _beta) :
    #theta = get_bloch_sphere_angles(_alpha, _beta)[0]
    #phi = get_bloch_sphere_angles(_alpha, _beta)[1]

    
    
    bpy.ops.object.select_all(action='DESELECT') #deselect all object

    #Sphere-------------------------------------------------------------
    mesh_sphere = bpy.data.meshes.new('Sphere')
    sphere = bpy.data.objects.new("Sphere", mesh_sphere)
    material_sphere = bpy.data.materials.new("MyMaterialSphere")
    material_sphere.diffuse_color = (0.37, 0.59, 0.9, 0.1)
    mesh_sphere.materials.append(material_sphere)
    #--------------------------------------------------------------------

    #Axes-------------------------------------------------------------
    mesh_axes = bpy.data.meshes.new('Axes')
    axes = bpy.data.objects.new("Axes", mesh_axes)
    material_axes = bpy.data.materials.new("MyMaterialAxes")
    material_axes.diffuse_color = (1., 1., 1., 1.)
    mesh_axes.materials.append(material_axes)
    #--------------------------------------------------------------------

    #Light_Axes-------------------------------------------------------------
    mesh_light_axes = bpy.data.meshes.new('LightAxes')
    light_axes = bpy.data.objects.new("LightAxes", mesh_light_axes)
    material_light_axes = bpy.data.materials.new("MyMaterialLightAxes")
    material_light_axes.diffuse_color = (0.2, 0.2, 0.2, 1.)
    mesh_light_axes.materials.append(material_light_axes)

    mesh_light_axes2 = bpy.data.meshes.new('LightAxes2')
    light_axes2 = bpy.data.objects.new("LightAxes2", mesh_light_axes2)
    mesh_light_axes2.materials.append(material_light_axes)
    #--------------------------------------------------------------------

    #Vector-------------------------------------------------------------
    mesh_vector = bpy.data.meshes.new('Vector')
    vector = bpy.data.objects.new("Vector", mesh_vector)
    material_vector = bpy.data.materials.new("MyMaterialVector")
    material_vector.diffuse_color = (0.73, 0.04, 0.04, 1.)
    mesh_vector.materials.append(material_vector)
    #--------------------------------------------------------------------

    #Bmesh sphere-------------------------------------------------------------
    bpy.context.collection.objects.link(sphere)
    bpy.context.view_layer.objects.active = sphere
    sphere.select_set(True)

    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments = 32, v_segments = 16, diameter = 2)
    bm.to_mesh(mesh_sphere)
    bm.free()
    bpy.ops.object.modifier_add(type = 'SUBSURF')
    bpy.ops.object.shade_smooth()
    #--------------------------------------------------------------------

    #Bmesh axes-------------------------------------------------------------
    bpy.context.collection.objects.link(axes)
    bpy.context.view_layer.objects.active = axes
    axes.select_set(True)

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'X'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'Y'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=12, diameter1=0.01, diameter2=0.01, depth=3.948)
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bm.to_mesh(mesh_axes)
    bm.free()
    #--------------------------------------------------------------------

    #Bmesh light axes----------------------------------------------------
    bpy.context.collection.objects.link(light_axes)
    bpy.context.view_layer.objects.active = light_axes
    light_axes.select_set(True)

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.915, diameter2=1.915, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.915, diameter2=1.915, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, -0.5)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, -1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.71, diameter2=1.71, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.71, diameter2=1.71, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, -1.)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, -1.5)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.29, diameter2=1.29, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.5)))
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.5)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.29, diameter2=1.29, depth=0.01)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, -1.5)))
    bm.to_mesh(mesh_light_axes)
    bm.free()

    bpy.context.collection.objects.link(light_axes2)
    bpy.context.view_layer.objects.active = light_axes2
    light_axes2.select_set(True)

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'Y'))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=40, diameter1=1.983, diameter2=1.983, depth=0.01)
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(math.radians(45.0), 3, 'Y'))
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'X'))
    bm.to_mesh(mesh_light_axes2)
    bm.free()
    #---------------------------------------------------------------------

    #Vector-------------------------------------------------------------
    bpy.context.collection.objects.link(vector)
    bpy.context.view_layer.objects.active = vector
    vector.select_set(True)

    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=20, diameter1=0.1, diameter2=0., depth=0.2)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 1.)))
    bmesh.ops.create_cone(bm, cap_ends=False, cap_tris=False, segments=20, diameter1=0.05, diameter2=0.05, depth=1.9)
    bmesh.ops.translate(bm, verts = bm.verts, vec = mathutils.Vector((0.0, 0.0, 0.95)))
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(theta, 3, 'Y'))
    bmesh.ops.rotate(bm, verts = bm.verts, cent =  (0.0, 0.0, 0.0), matrix=mathutils.Matrix.Rotation(phi, 3, 'Z'))
    bm.to_mesh(mesh_vector)
    bm.free()
    #--------------------------------------------------------------------
    
    #Text
    font_curve0 = bpy.data.curves.new(type="FONT",name="Font Curve 0")
    font_curve0.body = "|0>"
    font_obj0 = bpy.data.objects.new("Font Object 0", font_curve0)
    font_obj0.rotation_euler = (np.pi/2,0,np.pi*(3/4))
    font_obj0.scale = (0.5,0.5,0.5)
    font_obj0.location = (0.2, -0.2, 2.3 )
    bpy.context.collection.objects.link(font_obj0)
    bpy.context.view_layer.objects.active = font_obj0
    font_obj0.select_set(True)
    
    font_curve1 = bpy.data.curves.new(type="FONT",name="Font Curve 1")
    font_curve1.body = "|1>"
    font_obj1 = bpy.data.objects.new("Font Object 1", font_curve1)
    font_obj1.rotation_euler = (np.pi/2,0,np.pi*(3/4))
    font_obj1.scale = (0.5,0.5,0.5)
    font_obj1.location = (0.2, -0.2, -2.5 )
    bpy.context.collection.objects.link(font_obj1)
    bpy.context.view_layer.objects.active = font_obj1
    font_obj1.select_set(True)
    
    
    font_curvex = bpy.data.curves.new(type="FONT",name="Font Curve x")
    font_curvex.body = "x"
    font_objx = bpy.data.objects.new("Font Object x", font_curvex)
    font_objx.rotation_euler = (np.pi/2,0,0)
    font_objx.scale = (0.5,0.5,0.5)
    font_objx.location = ( 2.1, 0., 0. )
    bpy.context.collection.objects.link(font_objx)
    bpy.context.view_layer.objects.active = font_objx
    font_objx.select_set(True)
    
    font_curvey = bpy.data.curves.new(type="FONT",name="Font Curve y")
    font_curvey.body = "y"
    font_objy = bpy.data.objects.new("Font Object y", font_curvey)
    font_objy.rotation_euler = (np.pi/2,0,np.pi/2)
    font_objy.scale = (0.5,0.5,0.5)
    font_objy.location = ( 0. , 2.1, 0. )
    bpy.context.collection.objects.link(font_objy)
    bpy.context.view_layer.objects.active = font_objy
    font_objy.select_set(True)
    
    #Join all objects
    bpy.context.view_layer.objects.active = sphere 
    bpy.ops.object.join()
    
class BlochSphereNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_BlochSphereNode"
    bl_label = "Bloch Sphere"

    def create(self):
        self.newInput("Vector", "Output State", "output_state")
        self.newInput("Integer", "Qubit Index", "qubite_index", value = 0, minValue = 0)

    def execute(self, output_state, qubite_index):
        if output_state is None:
            return
        else :
            bloch_data = _bloch_multivector_data(output_state)
            bloch_sphere(output_state[qubite_index], output_state[qubite_index])