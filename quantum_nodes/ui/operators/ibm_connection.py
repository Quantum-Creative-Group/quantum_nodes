import bpy
from qiskit import IBMQ
from bpy.types import Operator
from bpy.props import PointerProperty
from .. properties.query_properties import QueryProperties


class IBMConnexion(Operator):
    """IBM credentials management panel."""

    bl_idname = "object.ibm_connexion"
    bl_label = "IBMConnexion"
    bl_description = "Enter your token to log yourself"
    query: PointerProperty(type=QueryProperties, name="Token") # noqa F821

    def execute(self, context):
        if bpy.context.scene.QueryProps.connected is False:
            try:
                bpy.context.scene.QueryProps.error_msg = ""
                IBMQ.enable_account(bpy.context.scene.QueryProps.query)
                bpy.context.scene.QueryProps.connected = True
                return {'FINISHED'}
            except Exception as e:
                if e.args[0].split(".")[4] == "connection":
                    bpy.context.scene.QueryProps.error_msg = "Please verify your internet connection"
                else:
                    bpy.context.scene.QueryProps.error_msg = e.args[0].split(".")[4]
                bpy.context.scene.QueryProps.connected = False
                return {'CANCELLED'}
        return {'FINISHED'}
