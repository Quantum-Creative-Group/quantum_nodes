import bpy
from bpy.types import Operator
from bpy.props import EnumProperty

def drawGatesOperator(self, context):
    dm = bpy.types.Scene.demo_manager
    for gate in dm.possible_gates:
        button = self.layout.operator('object.add_gate_button', text = gate)
        button.text = gate

class AddAndDelGate(Operator):
    bl_idname = "object.add_and_del_gate"
    bl_label = "Add And Delete Gate Operator"
    
    button: EnumProperty(
        items=[
            ('add', '+', '+', '', 0),
            ('del', '-', '-', '', 1),
        ],
        default='add'
    )

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and bpy.context.active_object == bpy.types.Scene.demo_manager.selected_obj

    def execute(self, context):
        dm = bpy.types.Scene.demo_manager
        if self.button == 'add':
            wm = bpy.context.window_manager
            wm.popup_menu(drawGatesOperator, title="Options")
        else: 
            dm.get_selected_circuit().del_gate(bpy.types.Object.select_index)
        return {'FINISHED'}

