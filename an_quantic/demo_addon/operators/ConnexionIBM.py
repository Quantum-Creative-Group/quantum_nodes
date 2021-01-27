import bpy
from qiskit import IBMQ
from bpy.types import Operator

class QueryProps(bpy.types.PropertyGroup):
    error_msg: bpy.props.StringProperty(default="")
    connected: bpy.props.BoolProperty(default=False)
    query: bpy.props.StringProperty(default="")
    
class ConnexionIBM(Operator):
    bl_idname = "object.connexion_ibm"
    bl_label = "ConnexionIBM"
    bl_description = "Enter your token to log yourself"
    query: bpy.props.PointerProperty(name="Token", type=QueryProps)

    def execute(self, context):
        if(bpy.context.scene.QueryProps.connected == False):
            try:
                bpy.context.scene.QueryProps.error_msg = ""
                IBMQ.enable_account(bpy.context.scene.QueryProps.query)
                bpy.context.scene.QueryProps.connected = True
                return {'FINISHED'}
            except Exception as e:
                bpy.context.scene.QueryProps.error_msg = e.args[0].split(".")[4]
                bpy.context.scene.QueryProps.connected = False
                return {'CANCELLED'}
        return {'FINISHED'}