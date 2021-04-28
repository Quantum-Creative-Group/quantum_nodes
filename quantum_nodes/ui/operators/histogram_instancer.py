from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.plot_empty_histogram import plotEmptyHistogram

class HistogramInstancer(Operator):
    bl_idname = "object.histogram_instancer"
    bl_label = "Create a new histogram"
    bl_description = "Plot an empty histogram.\nUse the corresponding node to start visualizing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyHistogram()
        return{'FINISHED'}