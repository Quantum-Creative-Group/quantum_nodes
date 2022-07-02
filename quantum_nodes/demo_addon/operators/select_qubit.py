import bpy
from bpy.types import Operator


def drawSelectQubitOperator(self, context):
    dm = bpy.types.Scene.demo_manager
    for i in range(dm.nb_qubits):
        button = self.layout.operator('object.select_qubit_button', text="q" + str(i + 1))
        button.index = i


class SelectQubit(Operator):
    bl_idname = "dialog.select_qubit"
    bl_label = "Select a qubit"
    bl_description = "Select the qubit you want to modify"

    @classmethod
    def poll(cls, context):
        if context.object is None:
            return False
        return (context.object.select_get()) and (bpy.context.active_object == bpy.types.Scene.demo_manager.target)

    def execute(self, context):
        wm = bpy.context.window_manager
        wm.popup_menu(drawSelectQubitOperator, title="Select a qubit")
        # Forces to redraw the view (magic trick)
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}
