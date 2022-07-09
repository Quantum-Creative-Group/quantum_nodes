import bpy
from bpy.types import Operator
from bpy.props import EnumProperty


def drawGatesOperator(self, context):
    dm = context.scene.demo_manager
    for gate in dm.possible_gates:
        button = self.layout.operator('object.add_gate_button', text=gate)
        button.text = gate


class AddAndDelGate(Operator):
    """Add / Remove a gate."""

    bl_idname = "object.add_and_del_gate"
    bl_label = "Add And Delete Gate Operator"
    bl_description = "Add/Remove Gates"

    button: EnumProperty(
        name="Edit", # noqa F821
        description="Add or remove quantum gates",
        items=[
            ('add', '+', '+', '', 0),  # noqa F821
            ('del', '-', '-', '', 1),  # noqa F821
        ],
    )

    @classmethod
    def poll(cls, context):
        if context.object is None:
            return False
        return (context.object.select_get()) and (context.active_object == context.scene.demo_manager.target)

    def execute(self, context):
        dm = context.scene.demo_manager
        if self.button == 'add':
            wm = bpy.context.window_manager
            wm.popup_menu(drawGatesOperator, title="Options")
            # Forces to redraw the view (magic trick)
            context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        else:
            dm.getSelectedCircuit().popGate(bpy.types.Object.select_index)
            dm.updateNodeTree()
        return {'FINISHED'}
