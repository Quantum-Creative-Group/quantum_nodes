import bpy
from qiskit import IBMQ
from bpy.types import Operator

class QueryProps(bpy.types.PropertyGroup):
    query: bpy.props.StringProperty(default="")

class ConnexionIBM(Operator):
    bl_idname = "object.connexion_ibm"
    bl_label = "ConnexionIBM"
    bl_description = "Enter your token to log yourself"
    query: bpy.props.PointerProperty(name="Token", type=QueryProps)

    def execute(self, context):
        try:
            IBMQ.enable_account(bpy.context.scene.QueryProps.query)
            return {'FINISHED'}
        except Exception as e:
            error_msg = ""
            for msg in e.args:
                error_msg += msg + "\n"
            print(error_msg)
            return {'CANCELLED'}