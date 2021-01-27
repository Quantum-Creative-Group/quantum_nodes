import bpy
from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.plotEmptyStateCity import plotEmptyStateCity

class StateCityInstancer(Operator):
    bl_idname = "object.state_city_instancer"
    bl_label = "Create a state city"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyStateCity()
        return{'FINISHED'}