import bpy
from qiskit import IBMQ
from bpy.types import Operator
from bpy.props import PointerProperty
from .. properties.QueryProperties import QueryProperties
    
class IBMConnexion(Operator):
    bl_idname = "object.ibm_connexion"
    bl_label = "IBMConnexion"
    bl_description = "Enter your token to log yourself"
    query: PointerProperty(name = "Token", type = QueryProperties)

    def execute(self, context):
        if context.scene.QueryProps.connected == False:
            try:
                context.scene.QueryProps.error_msg = ""
                IBMQ.enable_account(context.scene.QueryProps.query)
                context.scene.QueryProps.connected = True
                return {'FINISHED'}
            except Exception as e:
                context.scene.QueryProps.error_msg = e.args[0].split(".")[4]
                context.scene.QueryProps.connected = False
                return {'CANCELLED'}
        return {'FINISHED'}