import bpy
from animation_nodes.base_types import AnimationNode

class SchrodingerEquationSimulationNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SchrodingerEquationSimulation"
    bl_label = "Schrödinger Equation Simulation"

    def create(self):
        self.newInput("Integer", "Bonjour", "bonjour", minValue = 0, maxValue = 3)

    # def execute(self, source, target, offset):
    #     if source is None or target is None:
    #         return

    #     target.location = source.location + offset