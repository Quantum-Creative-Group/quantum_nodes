import numpy as np
import math
import bpy, os, sys
from .. lib import quantumblur
from . CircuitManager import CircuitManager
from . QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager

from bpy.props import(
    BoolProperty,
    FloatProperty,
    PointerProperty,
    IntProperty,
)
from bpy.types import(
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup,
)

class AddGateButton(bpy.types.Operator):
    bl_idname = "object.add_gate_button"
    bl_label = "AddGateButton"

    text: bpy.props.StringProperty(
        name = 'text',
        default = ''
    )

    def execute(self, context):
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        DEMO_Manager.get_selected_circuit().add_gate(bpy.types.Object.select_index-1, self.text)
        #print(DEMO_Manager.get_selected_circuit())

        return{'FINISHED'}

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

class NbQubitSetting(Operator):
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

class quantumize_op(Operator):
    bl_label = "Quantumize"
    bl_idname = "object.quantumize_op"
    bl_description = "Quantumizes the selected mesh"
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
        #print("nb of vertices = " + str(nb_vertices) + " ||||| nb of qubits = " + str(n))
            
        return {'FINISHED'}

class swap_to_an(bpy.types.Operator):
    bl_idname = "screen.swap_to_an"
    bl_label = "Add Material"
    bl_description = "Add New Material"

    def execute(self,context):
        bpy.ops.screen.space_type_set_or_cycle(space_type='NODE_EDITOR')
        #if bpy.types.Panel.bl_idname == 'AN_PT_tree_panel': print("coucou")            TESTER SI L'IDNAME CORRESPOND A ANIMATION NODE
        return {'FINISHED'}

class SelectAxis(bpy.types.PropertyGroup):
    axis = bpy.props.EnumProperty(
        items=[
            ('x', 'X', 'X', '', 0),
            ('y', 'Y', 'Y', '', 1),
            ('z', 'Z', 'Z', '', 2),
        ],
        default='x'
    )

class AddAndDelGate(bpy.types.Operator):
    bl_label = "AddAndDelGate"
    bl_idname = "object.add_and_del_gate"
    button = bpy.props.EnumProperty(
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
        #settings = context.scene.quantumize_settings
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if self.button == 'add':
            wm = bpy.context.window_manager
            wm.popup_menu(draw_func, title="Options")
            #DEMO_Manager.get_selected_circuit().add_gate(settings.nb_qubit-1, 'h') ######################### 'h' à modifier
        if self.button == 'del': 
            DEMO_Manager.get_selected_circuit().del_gate(bpy.types.Object.coucou-1)
        return{'FINISHED'}

class quantumize_ui(bpy.types.Panel):
    bl_label = "Quantumize"
    bl_idname = "quantumize_op"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QuantumMesh"

    obj_tmp = 'XXXXXXXXXXXXXXX'
    nb_qubits = 0

    bpy.types.Object.select_index = 1
    index_qubit = bpy.types.Object.select_index

    def addRow(self,n):
        layout = self.layout
        for i in range(n):
            row = layout.row()
        return row
    
    def draw(self, context):

        ####### __INIT__ #######

        layout = self.layout
        scene = context.scene
        obj = bpy.context.active_object
       
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager

        ####### DEFINE NB OF QUBITS FOR AN OBJECT #######

        if obj.name != self.obj_tmp: 
            self.obj_tmp = obj.name
            DEMO_Manager.nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))

        ####### UPDATE SELECTED CIRCUIT #######

        DEMO_Manager.selected_circuit = context.scene.axis_choice.axis 

        if context.object.select_get() == False or context.object.type != "MESH" or self.nb_qubits > 10:                                        
            bpy.context.active_object.select_set(False)
            self.nb_qubits = 0
        else : 
            self.nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))

        ####### SELECTED OBJECT #######

        row = self.addRow(1)
        row.label(text="Selected Object", icon="MESH_CUBE")
        row = self.addRow(1)
        row.prop(obj, "name")
        row = self.addRow(5)
       
        ####### SETTINGS #######
        
        row.label(text="Settings", icon="SETTINGS")
        row = self.addRow(3)

        ####### AXIS CHOICE #######

        row.label(text = "Axis", icon = 'ORIENTATION_LOCAL')
        row = self.addRow(1)
        row = layout.row()
        row.prop(context.scene.axis_choice, "axis", icon = 'ORIENTATION_LOCAL', expand = True)
        row = self.addRow(2)

        ####### QUBIT SELECTION #######

        row.label(text = "Select QuBit", icon = "LIGHTPROBE_GRID")
        index_qubit = bpy.types.Object.select_index
        row.operator('dialog.select_qubit', text = "ID = "+str(index_qubit), icon = "VIEWZOOM")
        row = self.addRow(3)
 
        ####### QUANTUM GATES #######
        
        row.label(text = "Quantum Gates", icon = 'SNAP_VERTEX')
        row = self.addRow(1)
        layout.operator('object.add_and_del_gate', text='+').button = 'add'
        layout.operator('object.add_and_del_gate', text='-').button = 'del'
        row = self.addRow(3)

        ####### DISPLAY #######
        
        if self.nb_qubits > 0:
            qindex = 0
            for qubit in DEMO_Manager.get_selected_circuit().data:
                qindex += 1
                gate_display = ""
                gate_display += "q" + str(qindex) + "  "
                for gate in qubit:
                    gate_display += "---|" + gate.upper() + "|---"
                row.label(text=gate_display)
                row = self.addRow(1)

        else :                                        
            bpy.context.active_object.select_set(False)
            self.nb_qubits = 0
            row.label(text="Select a correct object")
            row = self.addRow(2)

        ####### THE END #######

        row.operator(quantumize_op.bl_idname, text="Apply", icon="CHECKMARK")
        row = self.addRow(1)
        row.operator(swap_to_an.bl_idname, text="Advanced (Quantum Magic)", icon="PLUS")

        #######################

classes = (
    NbQubitSetting,
    SelectAxis,
    AddAndDelGate,
    quantumize_op,
    quantumize_ui,
)

def register():
    bpy.types.Scene.axis_choice = PointerProperty(type = SelectAxis)
    bpy.types.Scene.QuantumNodes_DEMO_Manager = QuantumNodes_DEMO_Manager()

if __name__ == "__main__":
    register()