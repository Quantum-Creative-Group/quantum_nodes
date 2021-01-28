from bpy.types import PropertyGroup
from bpy.props import (StringProperty, BoolProperty)

class QueryProps(PropertyGroup):
    error_msg: StringProperty(default="")
    connected: BoolProperty(default=False)
    query: StringProperty(default="")