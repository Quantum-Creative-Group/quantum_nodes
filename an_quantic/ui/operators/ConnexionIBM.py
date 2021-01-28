import bpy
from qiskit import IBMQ
from bpy.types import Operator
from .. properties.QueryProperties import QueryProps
    
class ConnexionIBM(Operator):
    bl_idname = "object.connexion_ibm"
    bl_label = "ConnexionIBM"
    bl_description = "Enter your token to log yourself"
    query: bpy.props.PointerProperty(name="Token", type=QueryProps)

    def execute(self, context):
        if bpy.context.scene.QueryProps.connected == False:
            try:
                bpy.context.scene.QueryProps.error_msg = ""
                IBMQ.enable_account(bpy.context.scene.QueryProps.query)
                bpy.context.scene.QueryProps.connected = True
                return {'FINISHED'}
            except Exception as e:
                if (e.args[0].split(".")[4] == "connection"):
                    bpy.context.scene.QueryProps.error_msg = "Please verify your internet connection"
                else:
                    bpy.context.scene.QueryProps.error_msg = e.args[0].split(".")[4]
                print(e.args)
                bpy.context.scene.QueryProps.connected = False
                return {'CANCELLED'}
        return {'FINISHED'}