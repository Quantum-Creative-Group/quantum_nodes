from bpy.types import PropertyGroup
from bpy.props import StringProperty, BoolProperty


class QueryProperties(PropertyGroup):
    """Query properties for IBM connection."""

    error_msg: StringProperty(
        name="Error message",  # noqa F821
        description="Content of the error message",
        default=""
    )

    connected: BoolProperty(
        name="Connected",  # noqa F821
        description="Indicate whether a connection is established or not",
        default=False,
    )

    query: StringProperty(
        name="Query",  # noqa F821
        description="Query",  # noqa F821
        default="",
    )
