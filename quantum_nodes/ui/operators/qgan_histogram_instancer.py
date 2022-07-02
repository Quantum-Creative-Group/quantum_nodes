from bpy.types import Operator
from bpy.props import StringProperty
from ... visualization.empty_graphs.qgan_plot_empty_histogram import plotEmptyQganHistogram


class HistogramInstancer(Operator):
    """Generate the example node tree which uses Quantum Blur."""

    bl_idname = "object.qgan_histogram_instancer"
    bl_label = "Create a new histogram for qGAN performance visualization"
    bl_description = "Plot an empty histogram.\nUse the corresponding node to start visualizing"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        plotEmptyQganHistogram()
        return{'FINISHED'}
