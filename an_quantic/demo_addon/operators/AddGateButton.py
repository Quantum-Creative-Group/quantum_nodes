import bpy
from bpy.types import Operator
from bpy.props import StringProperty

class AddGateButton(Operator):
    bl_idname = "object.add_gate_button"
    bl_label = "Add Gate Button Operator"
    
    text: StringProperty(name = 'text', default = '')

    def execute(self, context):
        dm = bpy.types.Scene.demo_manager
        dm.getSelectedCircuit().pushGate(bpy.types.Object.select_index, self.text)
        dm.updateNodeTree()
        return {'FINISHED'}