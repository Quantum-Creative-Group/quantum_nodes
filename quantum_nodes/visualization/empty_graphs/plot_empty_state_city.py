import bpy
import bmesh

from numpy import pi
from mathutils import Vector

from .. utils.graphs_utils import creatMultipleTextCity, creatMesh, historamCityDrawAxes


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
    X = size * 2
    Y = nb_cubes + 0.5
    Z = nb_cubes + 0.5
    T = 0.01
    # H = 0.25

    bpy.ops.object.select_all(action='DESELECT')  # deselect all object

    # Parent------------------------------------------------------------
    mesh_parent, parent = creatMesh("QuantumCityParent", 1., 1., 1., 0.)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bm.to_mesh(mesh_parent)
    bm.free()

    # Faces-------------------------------------------------------------
    mesh_faces, faces = creatMesh("QuantumCityFaces", 1., 1., 1., 1.)

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

    mesh_transparent_face, transparent_face = creatMesh("QuantumCityTransparentFace", 1., 1., 1., 0.1)

    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, Z, T)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(Y - 1.) / 2, Z / 2, size)))
    bm.to_mesh(mesh_transparent_face)
    bm.free()
    # --------------------------------------------------------------------

    # Axes-------------------------------------------------------------
    mesh_axes_front, axes_front = creatMesh("QuantumCityAxesFront", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_front, 19, T, Y, T, 0.0, 0.0, size / 10, -Y + 0.51, Y / 2, 0.0)

    mesh_axes_left, axes_left = creatMesh("QuantumCityAxesLeft", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_left, 19, Y, T, T, 0.0, 0.0, size / 10, -(Y - 1.) / 2, T, 0.0)

    mesh_axes_vertical_front, axes_vertical_front = creatMesh("QuantumCityAxesVerticalFront", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_vertical_front, nb_cubes, T, T, X, 0.0,
                         (Y - 0.5) / nb_cubes, 0.0, -Y + 0.51, -0.5, X / 2)

    mesh_axes_vertical_left, axes_vertical_left = creatMesh("QuantumCityAxesVerticalLeft", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_vertical_left, nb_cubes, T, T, X, (Y - 0.5) / nb_cubes, 0.0, 0.0, -Y, T, X / 2)

    mesh_axes_bottom_vertical, axes_bottom_vertical = creatMesh("QuantumCityAxesBottomVertical", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_bottom_vertical, nb_cubes, Y, T, T, 0.0,
                         (Y - 0.5) / nb_cubes, 0.0, -Y / 2 + 0.5, -0.5, T)

    mesh_axes_bottom_horizontal, axes_bottom_horizontal = creatMesh("QuantumCityAxesBottomHorizontal", 0., 0., 0., 1.)
    historamCityDrawAxes(mesh_axes_bottom_horizontal, nb_cubes, T, Y, T, (Y - 0.5) / nb_cubes, 0.0, 0.0, -Y, Z / 2, T)
    # --------------------------------------------------------------------

    # Text
    creatMultipleTextCity("QuantumHistogramCity", -Y + 0.5, Y + 0.1, pi / 2, 0, pi / 2, size)
    creatMultipleTextCity("QuantumHistogramCity", 1., 0.0, pi / 2, 0, pi, size)

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
