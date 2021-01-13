import bpy, colorsys
import numpy as np
from bpy.props import *
from animation_nodes.base_types import AnimationNode, VectorizedSocket

# using linear conversion here, unlike BL colorpicker hsv/hex
# BL Color() funcion does this also and has only rgb+hsv, so we'l use colorsys
# only hsv/hex in the colorpicker are gamma corrected for colorspaces
# we shall not use other functions, till they are in context (BL color space)

targetTypeItems = [
    ("RGB", "RGB", "Red, Green, Blue"),
    ("HSL", "HSL", "Hue, Saturation, Lightness"),]

class SchrodingerToColorNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_SchrodingerToColorNode"
    bl_label = "Schrödinger Complex To Color"
    dynamicLabelType = "HIDDEN_ONLY"

    useList: VectorizedSocket.newProperty()

    targetType: EnumProperty(name = "Target Type", items = targetTypeItems,
        default = "RGB", update = AnimationNode.refresh)

    def create(self):
        self.newInput(VectorizedSocket("Matrix", "useList", ("Schrödinger Matrix", "schrodinger_matrix"), ("Schrödinger Matrix", "schrodinger_matrix")))
        self.newInput()
            
    def draw(self, layout):
        layout.prop(self, "targetType", expand = True)

    def drawLabel(self):
        return "{}A from Color".format(self.targetType)

    def drawAdvanced(self, layout):
        layout.label(text = "Uses linear color space", icon = "INFO")

    def gexecute(self):
        if schrodinger_matrix is None:
            return 0

        arg = np.angle(schrodinger_complex)

        h = (arg + np.pi) / (2 * np.pi) + 0.5
        l = 1.0 - 1.0/(1.0 + 2*r**1.2)
        s = saturation

        c = np.vectorize(hls_to_rgb) (h,l,s) 
        c = np.array(c)
        c = c.swapaxes(0,2)
        c = c.swapaxes(0,1)
        return c

    def getUsedModules(self):
        return ["colorsys"]
