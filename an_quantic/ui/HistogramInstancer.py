import bpy
from bpy.types import Operator
from bpy.props import StringProperty
# from .. visualization.bloch_sphere_visualization import bloch_sphere

class HistogramInstancer(Operator):
    bl_idname = "object.histogram_instancer"
    bl_label = "Create a new histogram"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Et voilà, un nouvel histogram !")
        return{'FINISHED'}