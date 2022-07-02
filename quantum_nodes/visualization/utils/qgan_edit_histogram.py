import bpy
import bmesh
from mathutils import Vector
from numpy import pi
from qiskit.visualization.utils import _bloch_multivector_data
from .graphs_utils import creatMesh, creatMultipleText


def editQganHistogram(parent, _targetCounts, _simulationCounts):
    # data
    targetKeys = list(_targetCounts)
    simulationKeys = list(_simulationCounts)
    nb_cubes = len(targetKeys)  # Nb of rectangles (for each quantity, i.e. target and simulation) in the histogram
    X = 3.2
    Y = 0.7
    Z = nb_cubes
    T = 0.01
    H = 0.25
    size = 3

    bpy.ops.object.select_all(action='DESELECT')  # deselect all object

    # Target Cubes-------------------------------------------------------------
    mesh_cube, cube = creatMesh("QuantumQganHistogramCubes", 1., 0., 0., 0.9)

    bm = bmesh.new()  # create an empty BMesh
    for i in range(nb_cubes):
        scale = _targetCounts[targetKeys[i]]
        resize = 0.5 / (scale * size)
        if i != 0:
            bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 1.0, 0.0)))
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / resize, 1 / resize, 1)))
            bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, (-scale * size) / 2)))
        bmesh.ops.create_cube(bm, size=scale * size)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((resize, resize, 1.)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, (scale * size) / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.5, 0.0)))
    bm.to_mesh(mesh_cube)  # write the bmesh back to the mesh
    bm.free()  # free and prevent further access
    # --------------------------------------------------------------------

    # Simulation Cubes-------------------------------------------------------------
    mesh_cube, cube = creatMesh("QuantumQganHistogramCubes", 0., 0., 1., 0.9)

    bm = bmesh.new()  # create an empty BMesh
    for i in range(nb_cubes):
        scale = _simulationCounts[simulationKeys[i]]
        resize = 0.5 / (scale * size)
        if i != 0:
            bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 1.0, 0.0)))
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / resize, 1 / resize, 1)))
            bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, (-scale * size) / 2)))
        bmesh.ops.create_cube(bm, size=scale * size)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((resize, resize, 1.)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, (scale * size) / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.5, 0.0)))
    bm.to_mesh(mesh_cube)  # write the bmesh back to the mesh
    bm.free()  # free and prevent further access
    # --------------------------------------------------------------------

    # Faces-------------------------------------------------------------
    mesh_faces, faces = creatMesh("QuantumQganHistogramFaces", 1., 1., 1., 1.)

    bm = bmesh.new()

    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, Z, X)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-H, Z / 2, X / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-0.1, 0.0, -X / 2)))
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / T, 1 / X)))

    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, T, X)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.1, 0.0, X / 2)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-0.1, -Z / 2, 0.0)))
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / Z, 1 / T)))

    bmesh.ops.create_cube(bm, size=1)
    bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, Z, T)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.1, Z / 2, 0.0)))

    bm.to_mesh(mesh_faces)
    bm.free()
    # --------------------------------------------------------------------

    # Axes-------------------------------------------------------------
    mesh_axes_front, axes_front = creatMesh("QuantumQganHistogramAxesFront", 0., 0., 0., 1.)

    bm = bmesh.new()
    for i in range(10):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / T, 1 / nb_cubes, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((T, nb_cubes, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, size / 10)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((-(H - T), nb_cubes / 2, 0.0)))
    bm.to_mesh(mesh_axes_front)
    bm.free()

    mesh_axes_left, axes_left = creatMesh("QuantumQganHistogramAxesFront", 0., 0., 0., 1.)

    bm = bmesh.new()
    for i in range(10):
        if i != 0:
            bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((1 / Y, 1 / T, 1 / T)))
        bmesh.ops.create_cube(bm, size=1)
        bmesh.ops.scale(bm, verts=bm.verts, vec=Vector((Y, T, T)))
        bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.0, 0.0, size / 10)))
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0.1, T, 0.0)))
    bm.to_mesh(mesh_axes_left)
    bm.free()
    # --------------------------------------------------------------------

    # Text
    creatMultipleText("QuantumQganHistogramFontRight", -0.25, nb_cubes + 0.1, pi / 2, 0, pi / 2, size)
    creatMultipleText("QuantumQganHistogramFontLeft", Y + 0.1, 0.0, pi / 2, 0, pi, size)

    curves_results_diffs = {}
    text_objects_results_diffs = {}
    for i in range(nb_cubes):  # or nb_cubes, 0, -1
        # Difference between target and simulation "probabilities"
        targetSimuDiff = _simulationCounts[simulationKeys[i]] - _targetCounts[targetKeys[i]]
        # To place diff value at the top of each rectangle
        targetSimuMax = max(_targetCounts[targetKeys[i]], _simulationCounts[simulationKeys[i]])
        curves_results_diffs["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_results_diffs["font_curve_{0}".format(i)].body = str(targetSimuDiff)
        text_objects_results_diffs["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_results_diffs["font_curve_{0}".format(i)])
        text_objects_results_diffs["font_obj_{0}".format(i)].rotation_euler = (
            pi / 2, -pi / 2, pi / 2)  # not this pi is the problem
        text_objects_results_diffs["font_obj_{0}".format(i)].scale = (0.2, 0.2, 0.2)
        text_objects_results_diffs["font_obj_{0}".format(i)].location = (
            0.05, (nb_cubes - i) - 0.4, targetSimuMax * size + 0.2)
        bpy.context.collection.objects.link(text_objects_results_diffs["font_obj_{0}".format(i)])
        bpy.context.view_layer.objects.active = text_objects_results_diffs["font_obj_{0}".format(i)]
        text_objects_results_diffs["font_obj_{0}".format(i)].select_set(True)

    curves_results = {}
    text_objects_results = {}
    for i in range(nb_cubes):  # or nb_cubes, 0, -1
        curves_results["font_curve_{0}".format(i)] = bpy.data.curves.new(type="FONT", name="Font Curve" + str(i))
        curves_results["font_curve_{0}".format(i)].body = targetKeys[i]
        text_objects_results["font_obj_{0}".format(i)] = bpy.data.objects.new(
            "Font Object" + str(i), curves_results["font_curve_{0}".format(i)])
        # x = pi/2 is for the correct direction
        text_objects_results["font_obj_{0}".format(i)].rotation_euler = (-pi / 2, -pi, -pi / 2)
        text_objects_results["font_obj_{0}".format(i)].scale = (0.2, 0.2, 0.2)
        text_objects_results["font_obj_{0}".format(i)].location = (
            Y + 0.01, (nb_cubes - i) - 0.7, 0.0)  # 3rd arg was 0.0
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
