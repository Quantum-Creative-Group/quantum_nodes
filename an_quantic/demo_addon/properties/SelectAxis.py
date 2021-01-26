from bpy.types import PropertyGroup
from bpy.props import EnumProperty

class SelectAxis(PropertyGroup):
    axis: EnumProperty(
        items=[
            ('x', 'X', 'X', '', 0),
            ('y', 'Y', 'Y', '', 1),
            ('z', 'Z', 'Z', '', 2),
        ],
        default='x'
    )