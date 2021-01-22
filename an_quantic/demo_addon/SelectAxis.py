import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur

class SelectAxis(bpy.types.PropertyGroup):
    axis = bpy.props.EnumProperty(
        items=[
            ('x', 'X', 'X', '', 0),
            ('y', 'Y', 'Y', '', 1),
            ('z', 'Z', 'Z', '', 2),
        ],
        default='x'
    )