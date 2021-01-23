from bpy.types import Operator

class ApplyQuantumCircuit(Operator):
    bl_label = "ApplyQuantumCircuit"
    bl_idname = "object.apply_quantum_circuit"
    bl_description = "Applies the quantum circuit on the selected mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"
    
    def execute(self, context):
        return {'FINISHED'}