from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.plot_empty_state_city import plotEmptyStateCity


class StateCityInstancer(Operator):
    """Generate a new state city plot for data visualization."""

    bl_idname = "object.state_city_instancer"
    bl_label = "Create a state city"
    bl_description = "WIP : Plot empty state city"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return False

    def execute(self, context):
        plotEmptyStateCity()
        return{'FINISHED'}
