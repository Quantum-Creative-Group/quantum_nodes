from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.plot_empty_bloch_sphere import plotEmptyBlochSphere


class BlochSphereInstancer(Operator):
    bl_idname = "object.bloch_sphere_instancer"
    bl_label = "Create a new Bloch sphere"
    bl_description = "Plot an empty Bloch sphere.\nUse the corresponding node to start visualizing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyBlochSphere()
        return{'FINISHED'}
