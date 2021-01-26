import bpy
from bpy.types import Operator
from bpy.props import StringProperty
# from .. visualization.bloch_sphere_visualization import bloch_sphere

class StateCityInstancer(Operator):
    bl_idname = "object.state_city_instancer"
    bl_label = "Create a state city"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Et voilà, un nouveau state city !")
        return{'FINISHED'}