import bpy, os, sys
from . NbQubitSettings import draw_func, setSliderValue, getSliderValue

class AddGateButton(bpy.types.Operator):
    bl_idname = "object.add_gate_button"
    bl_label = "Add Gate Button Operator"
    
    text: bpy.props.StringProperty(
        name = 'text',
        default = ''
    )

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        DEMO_Manager.get_selected_circuit().add_gate(bpy.types.Object.select_index-1, self.text)
        return{'FINISHED'}