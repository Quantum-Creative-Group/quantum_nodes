import bpy
import bmesh

import numpy as np
from numpy import pi
from mathutils import Vector
from qiskit.quantum_info.states import DensityMatrix


def editStateCity(parent, state):
    rho = DensityMatrix(state)
    num = rho.num_qubits
    if num is None:
        raise RuntimeError("Input is not a multi-qubit quantum state.")

    # data
    datareal = np.real(rho.data)
    nb_cubes = len(datareal)

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
    X = size * 2
    Y = nb_cubes + 0.5
    Z = nb_cubes + 0.5
    T = 0.01
    # H = 0.25
    column_names = [bin(i)[2:].zfill(num) for i in range(2**num)]
    row_names = [bin(i)[2:].zfill(num) for i in range(2**num)]
    bpy.ops.object.select_all(action='DESELECT')  # deselect all object

    # Cubes-------------------------------------------------------------
    material_cube = bpy.data.materials.new("MyMaterialCube")
    material_cube.diffuse_color = (0.45, 0.258, 0.784, 1.)

    for i in range(nb_cubes):
        mesh_cube = bpy.data.meshes.new('Cube')
        cube = bpy.data.objects.new("Cube", mesh_cube)
        mesh_cube.materials.append(material_cube)

        bpy.context.collection.objects.link(cube)
        bpy.context.view_layer.objects.active = cube
        cube.select_set(True)
        bm = bmesh.new()
        print(nb_cubes)
        for j in range(nb_cubes):
            scale = datareal[i][nb_cubes - j - 1]
            if scale == 0:
                resize = 0.5 / 0.001
                cube_size = 0.001
            else:
                cube_size = scale * size
                resize = 0.5 / cube_size
            translate = cube_size / 2
            if j != 0:
                bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-1.0, 0.0, 0.0)))
                bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / resize, 1 / resize, 1)))
                bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, -translate)))
            bmesh.ops.create_cube(bm, size=cube_size)
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((resize, resize, 1.)))
            bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, translate)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-0.5, i + 0.5, size)))
        bm.to_mesh(mesh_cube)
        bm.free()
    # --------------------------------------------------------------------

    # Faces-------------------------------------------------------------
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
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, Z, X)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y + 0.5, Z / 2, X / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(((Y - 1.) / 2, 0.0, -X / 2)))
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / T, 1 / X)))
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, T, X)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(Y - 1.) / 2, 0.0, X / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(((Y - 1.) / 2, -Z / 2, 0.0)))
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / Z, 1 / T)))
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, Z, T)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(Y - 1.) / 2, Z / 2, 0.0)))
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
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, Z, T)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(Y - 1.) / 2, Z / 2, size)))
    bm.to_mesh(mesh_transparent_face)
    bm.free()
    # --------------------------------------------------------------------

    # Axes-------------------------------------------------------------
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
    for i in range(19):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / T, 1 / Y, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, Y, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, size / 10)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y + 0.51, Y / 2, 0.0)))
    bm.to_mesh(mesh_axes_front)
    bm.free()

    bpy.context.collection.objects.link(axes_left)
    bpy.context.view_layer.objects.active = axes_left
    axes_left.select_set(True)

    bm = bmesh.new()
    for i in range(19):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / T, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, T, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, size / 10)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(Y - 1.) / 2, T, 0.0)))
    bm.to_mesh(mesh_axes_left)
    bm.free()

    bpy.context.collection.objects.link(axes_vertical_front)
    bpy.context.view_layer.objects.active = axes_vertical_front
    axes_vertical_front.select_set(True)

    bm = bmesh.new()
    for i in range(nb_cubes):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / T, 1 / T, 1 / X)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, T, X)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, (Y - 0.5) / nb_cubes, 0.0)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y + 0.51, -0.5, X / 2)))
    bm.to_mesh(mesh_axes_vertical_front)
    bm.free()

    bpy.context.collection.objects.link(axes_vertical_left)
    bpy.context.view_layer.objects.active = axes_vertical_left
    axes_vertical_left.select_set(True)

    bm = bmesh.new()
    for i in range(nb_cubes):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / T, 1 / T, 1 / X)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, T, X)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(((Y - 0.5) / nb_cubes, 0.0, 0.0)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y, T, X / 2)))
    bm.to_mesh(mesh_axes_vertical_left)
    bm.free()

    bpy.context.collection.objects.link(axes_bottom_vertical)
    bpy.context.view_layer.objects.active = axes_bottom_vertical
    axes_bottom_vertical.select_set(True)

    bm = bmesh.new()
    for i in range(nb_cubes):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / T, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, T, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, (Y - 0.5) / nb_cubes, 0.0)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y / 2 + 0.5, -0.5, T)))
    bm.to_mesh(mesh_axes_bottom_vertical)
    bm.free()

    bpy.context.collection.objects.link(axes_bottom_horizontal)
    bpy.context.view_layer.objects.active = axes_bottom_horizontal
    axes_bottom_horizontal.select_set(True)

    bm = bmesh.new()
    for i in range(nb_cubes):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / T, 1 / Y, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, Y, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(((Y - 0.5) / nb_cubes, 0.0, 0.0)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-Y, Z / 2, T)))
    bm.to_mesh(mesh_axes_bottom_horizontal)
    bm.free()

    # --------------------------------------------------------------------

    # Text
    curves_front = {}
    text_objects_front = {}
    for i in range(21):
        curves_front["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        if i < 10:
            curves_front["font_curve_{0}".format(i)].body = str(-(10 - i) / 10)
        else:
            curves_front["font_curve_{0}".format(i)].body = str((i - 10) / 10)
        text_objects_front["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_front["font_curve_{0}".format(i)])
        text_objects_front["font_obj_{0}".format(i)].rotation_euler = (pi / 2, 0, pi / 2)
        text_objects_front["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_front["font_obj_{0}".format(i)].location = (-Y + 0.5, Y + 0.1, (size * i) / 10 - 0.07)
        bpy.context.collection.objects.link(text_objects_front["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_front["font_obj_{0}".format(i)]
        text_objects_front["font_obj_{0}".format(i)].select_set(True)

    curves_left = {}
    text_objects_left = {}
    for i in range(21):
        curves_left["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        if i < 10:
            curves_left["font_curve_{0}".format(i)].body = str(-(10 - i) / 10)
        else:
            curves_left["font_curve_{0}".format(i)].body = str((i - 10) / 10)
        text_objects_left["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_left["font_curve_{0}".format(i)])
        text_objects_left["font_obj_{0}".format(i)].rotation_euler = (pi / 2, 0, pi)
        text_objects_left["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_left["font_obj_{0}".format(i)].location = (1., 0.0, (size * i) / 10 - 0.07)
        bpy.context.collection.objects.link(text_objects_left["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_left["font_obj_{0}".format(i)]
        text_objects_left["font_obj_{0}".format(i)].select_set(True)

    curves_resuts_right = {}
    text_objects_resuts_right = {}
    for i in range(nb_cubes):
        curves_resuts_right["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_resuts_right["font_curve_{0}".format(i)].body = column_names[i]
        text_objects_resuts_right["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_resuts_right["font_curve_{0}".format(i)])
        text_objects_resuts_right["font_obj_{0}".format(i)].rotation_euler = (0, 0, pi)
        text_objects_resuts_right["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_resuts_right["font_obj_{0}".format(i)].location = (
            (0.2) * num + 0.5, i * ((Y - 0.5) / nb_cubes) + 0.6, 0.0)
        bpy.context.collection.objects.link(text_objects_resuts_right["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_resuts_right["font_obj_{0}".format(i)]
        text_objects_resuts_right["font_obj_{0}".format(i)].select_set(True)

    curves_resuts_right = {}
    text_objects_resuts_right = {}
    for i in range(nb_cubes):
        curves_resuts_right["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_resuts_right["font_curve_{0}".format(i)].body = column_names[i]
        text_objects_resuts_right["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_resuts_right["font_curve_{0}".format(i)])
        text_objects_resuts_right["font_obj_{0}".format(i)].rotation_euler = (0, 0, pi)
        text_objects_resuts_right["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_resuts_right["font_obj_{0}".format(i)].location = (
            (0.2) * num + 0.5, i * ((Y - 0.5) / nb_cubes) + 0.6, X / 2)
        bpy.context.collection.objects.link(text_objects_resuts_right["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_resuts_right["font_obj_{0}".format(i)]
        text_objects_resuts_right["font_obj_{0}".format(i)].select_set(True)

    curves_resuts_right = {}
    text_objects_resuts_right = {}
    for i in range(nb_cubes):
        curves_resuts_right["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_resuts_right["font_curve_{0}".format(i)].body = row_names[i]
        text_objects_resuts_right["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_resuts_right["font_curve_{0}".format(i)])
        text_objects_resuts_right["font_obj_{0}".format(i)].rotation_euler = (0, 0, -pi / 2)
        text_objects_resuts_right["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_resuts_right["font_obj_{0}".format(
            i)].location = (-i * ((Y - 0.5) / nb_cubes) - 0.6, Z + ((0.3) * num + 0.5) / 2, 0.0)
        bpy.context.collection.objects.link(text_objects_resuts_right["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_resuts_right["font_obj_{0}".format(i)]
        text_objects_resuts_right["font_obj_{0}".format(i)].select_set(True)

    curves_resuts_right = {}
    text_objects_resuts_right = {}
    for i in range(nb_cubes):
        curves_resuts_right["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_resuts_right["font_curve_{0}".format(i)].body = row_names[i]
        text_objects_resuts_right["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_resuts_right["font_curve_{0}".format(i)])
        text_objects_resuts_right["font_obj_{0}".format(i)].rotation_euler = (0, 0, -pi / 2)
        text_objects_resuts_right["font_obj_{0}".format(i)].scale = (0.3, 0.3, 0.3)
        text_objects_resuts_right["font_obj_{0}".format(
            i)].location = (-i * ((Y - 0.5) / nb_cubes) - 0.6, Z + ((0.3) * num + 0.5) / 2, X / 2)
        bpy.context.collection.objects.link(text_objects_resuts_right["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_resuts_right["font_obj_{0}".format(i)]
        text_objects_resuts_right["font_obj_{0}".format(i)].select_set(True)

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
