from bpy.types import Operator
from bpy.props import PointerProperty

from qiskit import IBMQ

from .. properties.query_properties import QueryProperties


class IBMConnection(Operator):
    """IBM credentials management panel."""

    bl_idname = "object.ibm_connection"
    bl_label = "IBMConnection"
    bl_description = "Enter your token to log yourself"

    query: PointerProperty(type=QueryProperties)

    def execute(self, context):
        if context.scene.QueryProps.connected is False:
            try:
                context.scene.QueryProps.error_msg = ""
                IBMQ.enable_account(context.scene.QueryProps.query)
                context.scene.QueryProps.connected = True
                return {'FINISHED'}
            except Exception as e:
                if e.args[0].split(".")[4] == "connection":
                    context.scene.QueryProps.error_msg = "Please verify your internet connection"
                else:
                    context.scene.QueryProps.error_msg = e.args[0].split(".")[4]
                context.scene.QueryProps.connected = False
                return {'CANCELLED'}
        return {'FINISHED'}
