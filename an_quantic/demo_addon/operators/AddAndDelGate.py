import bpy, os, sys
from . NbQubitSettings import draw_func, setSliderValue, getSliderValue

class AddAndDelGate(bpy.types.Operator):
    bl_idname = "object.add_and_del_gate"
    bl_label = "Add And Delete Gate Operator"
    
    button: bpy.props.EnumProperty(
        items=[
            ('add', '+', '+', '', 0),
            ('del', '-', '-', '', 1),
        ],
        default='add'
    )

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if self.button == 'add':    
            wm = bpy.context.window_manager
            wm.popup_menu(draw_func, title="Options")
        else: 
            DEMO_Manager.get_selected_circuit().del_gate(bpy.types.Object.select_index-1)

        return {'FINISHED'}

