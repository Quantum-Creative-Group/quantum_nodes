from bpy.types import PropertyGroup
from bpy.props import EnumProperty


class SelectAxis(PropertyGroup):
    """Select axis property."""

    axis: EnumProperty(
        name="Axis",  # noqa F821
        description="Axis on which edit the quantum circuit",
        items=[
            ('x', 'X', 'X', '', 0),  # noqa F821
            ('y', 'Y', 'Y', '', 1),  # noqa F821
            ('z', 'Z', 'Z', '', 2),  # noqa F821
        ],
        default='x'  # noqa F821
    )
