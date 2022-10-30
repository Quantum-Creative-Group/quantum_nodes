from bpy.types import Operator

from .. visualization.empty_graphs.plot_empty_histogram import plotEmptyHistogram


class HistogramInstancer(Operator):
    """Generate a new histogram for data visualization."""

    bl_idname = "object.histogram_instancer"
    bl_label = "Create a new histogram"
    bl_description = "Plot an empty histogram.\nUse the corresponding node to start visualizing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyHistogram()
        return {'FINISHED'}
