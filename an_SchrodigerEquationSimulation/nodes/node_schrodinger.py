import bpy
from animation_nodes.base_types import AnimationNode

from .. algorithms.schrodinger_equation.SimulationManager import SimulationManager

class SchrodingerEquationSimulationNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SchrodingerEquationSimulation"
    bl_label = "Schrödinger Equation Simulation"
    errorHandlingType = "EXCEPTION"
    _sse = SimulationManager(10, 5, [-5.0, 0.0], [1.0, 0.0], [0.5, 0.5], "0", "False", 25, 10, 0.125)

    def create(self):
        self.newInput("Integer", "Frame rate", "frame_rate", value = 25, minValue = 0)
        self.newInput("Float", "Duration", "duration", value = 5, minValue = 0)
        self.newInput("Float", "Δt", "delta_t", value = 0.125, minValue = 0)

        self.newInput("Integer", "Dimension (N)", "dimension", value = 10, minValue = 1)
        self.newInput("Integer", "Size", "size", value = 10, minValue = 0)

        self.newInput("Vector 2D", "Center", "center", value = (-5., 0.))
        self.newInput("Vector 2D", "Number of waves", "number_of_waves", value = (1., 0.))
        self.newInput("Vector 2D", "Sprawl", "sprawl", value = (0.5, 0.5))

        self.newInput("Text", "Potential", "potential", value = "0")
        self.newInput("Text", "Obstacle.s", "obstacles", value = "False")

        self.newOutput("Complex128 List", "Output", "output")
        self.newOutput("Integer", "Offset", "offset")

    def execute(self, frame_rate, duration, delta_t, dimension, size, center, number_of_waves, sprawl, potential, obstacles):
        try:
            self._sse.updateSimulation(dimension, size, center, number_of_waves, sprawl, potential, obstacles, frame_rate, duration, delta_t)
            return (self._sse.getFrameData(bpy.data.scenes['Scene'].frame_current), dimension)
        except Exception as e:
            error_msg = ""
            for msg in e.args:
                error_msg += msg + "\n"
            self.raiseErrorMessage(error_msg)
            