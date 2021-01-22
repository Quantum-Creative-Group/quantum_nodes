import bpy
from bpy.types import Operator
import math

class ApplyQuantumCircuit(Operator):
    bl_label = "AppluQuantumCircuit"
    bl_idname = "object.apply_quantum_circuit"
    bl_description = "Applies the quantum circuit on the selected mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"
    
    def execute(self, context):
        scene = bpy.context.scene
        #settings = scene.quantumize_settings
        
        obj = context.object
        me = obj.data
        nb_vertices = (len(me.vertices))
        n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
            
        return {'FINISHED'}