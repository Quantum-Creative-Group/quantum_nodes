import bpy
from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.plotEmptyBlochSphere import plotEmptyBlochSphere

class BlochSphereInstancer(Operator):
    bl_idname = "object.bloch_sphere_instancer"
    bl_label = "Create a new Bloch sphere"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyBlochSphere()
        return{'FINISHED'}