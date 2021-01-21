import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur
from bpy.types import(
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup,
)

def draw_func(self, context):
    layout = self.layout

    button1 = layout.operator('object.add_gate_button', text = 'h')
    button1.text = 'h'
    button2 = layout.operator('object.add_gate_button', text = 'x')
    button2.text = 'x'
    button3 = layout.operator('object.add_gate_button', text = 'y')
    button3.text = 'y'

def setSliderValue(self, value):
    DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
    m = DEMO_Manager.nb_qubits

    if 1<=value<=m : return value
    elif value < 1 : return 1
    else : return m
    #return self
    
def getSliderValue(self):
    return self

class NbQubitSettings(Operator):
    bl_label = "Select Qubit"
    bl_idname = "dialog.select_qubit"

    n = bpy.props.IntProperty(name="Select QuBit Index", default=1)

    @classmethod
    def poll(cls, context):
        return context.object.select_get() and context.object.type == "MESH"

    def execute(self, context):
        bpy.types.Object.select_index = setSliderValue(self.n, getSliderValue(self.n))
        return {'FINISHED'}

    def invoke(self, context, event):    
        return context.window_manager.invoke_props_dialog(self)