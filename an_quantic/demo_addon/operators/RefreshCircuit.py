import bpy
from bpy.types import Operator

class RefreshCircuit(Operator):
    bl_idname = "object.refresh_quantum_circuit"
    bl_label = "Refresh Circuit"
    bl_description = "Refreshes every node trees"
    
    def execute(self, context):
        print("mdr")
        return{'FINISHED'}