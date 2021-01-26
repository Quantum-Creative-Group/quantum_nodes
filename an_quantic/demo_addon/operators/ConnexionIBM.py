import bpy
from qiskit import IBMQ
from bpy.types import Operator

class QueryProps(bpy.types.PropertyGroup):

    query: bpy.props.StringProperty(default="")

class ConnexionIBM(Operator):
    bl_idname = "object.connexion_ibm"
    bl_label = "ConnexionIBM"
    bl_description = "Enter your token to log yourself"

    def execute(self, context):
        try:
            bpy.data.objects[self.token].select_set(True)
            IBMQ.enable_account(self.token)
            return {'FINISHED'}
        except:
            print('Could not select object')
            return {'CANCELLED'}