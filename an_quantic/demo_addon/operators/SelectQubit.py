import bpy, os, sys
from bpy.types import(
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup,
)

def drawSelectQubitOperator(self, context):
    layout = self.layout

    dm = bpy.types.Scene.QuantumNodes_DEMO_Manager
    for i in range(dm.nb_qubits):
        button = layout.operator('object.select_qubit_button', text = "q"+str(i+1))
        button.index = i

class SelectQubit(Operator):
    bl_idname = "dialog.select_qubit"
    bl_label = "Select a qubit"

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"

    def execute(self, context):
        wm = bpy.context.window_manager
        wm.popup_menu(drawSelectQubitOperator, title="Select a qubit")
        # TADAAAAAAAAAAA CALL ME HOUDINI (forces to refresh)
        bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
        return {'FINISHED'}