import bpy

from animation_nodes.base_types import AnimationNode

class SchrodingerEquationSimulationNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SchrodingerEquationSimulation"
    bl_label = "Schrödinger Equation Simulation"

    def create(self):
        self.newInput("Integer", "Frame rate", "frame_rate", value = 25, minValue = 0)
        self.newInput("Float", "Duration", "duration", value = 5, minValue = 0)
        self.newInput("Float", "Δt", "Δt", value = 0.13, minValue = 0)

        self.newInput("Integer", "Dimension (N)", "dimension_N", value = 10, minValue = 1)
        self.newInput("Integer", "Size", "size", value = 5, minValue = 0)

        self.newInput("Vector", "Center", "center", value = (5.,2.,3.))
        self.newInput("Vector", "Number of waves", "number_of_waves")
        self.newInput("Vector", "Sprawl", "sprawl")

        self.newInput("Boolean", "Potential", "potential", value = 0)
        self.newInput("Boolean", "Obstacle.s", "obstacles", value = 0)

        self.newOutput("Matrix", "Output", "output")

    # def execute(self, source, target, offset):
    #     if source is None or target is None:
    #         return

    #     target.location = source.location + offset