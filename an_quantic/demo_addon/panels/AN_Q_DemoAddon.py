import math
import bpy, os, sys

from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager
from .. properties.SelectAxis import SelectAxis
from .. operators.SwapToAn import SwapToAn
from .. operators.AddGateButton import AddGateButton
from .. operators.AddAndDelGate import AddAndDelGate
from .. operators.SelectObject import *
from .. operators.NbQubitSettings import NbQubitSettings, draw_func, setSliderValue, getSliderValue
from .. operators.ApplyQuantumCircuit import ApplyQuantumCircuit

from bpy.props import PointerProperty
from bpy.types import Panel

class AN_Q_DemoAddon(bpy.types.Panel):
    bl_idname = "AN_Q_PT_addon_demo_ui"
    bl_label = "AN_Q Demo addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AN_Q_DEMO"

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
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager

        if DEMO_Manager.selected_obj == None:
            DEMO_Manager.createNewCircuit(bpy.context.active_object)

        obj = DEMO_Manager.selected_obj

        ####### DEFINE NB OF QUBITS FOR AN OBJECT #######
        if obj.name != self.obj_tmp and obj.type == "MESH":
            self.obj_tmp = obj.name
            # DEMO_Manager.createNewCircuit(obj)

        ####### UPDATE SELECTED CIRCUIT #######

        DEMO_Manager.selected_circuit = context.scene.axis_choice.axis

        if context.object.select_get() == False or context.object.type != "MESH" or self.nb_qubits > 10:
            # bpy.context.active_object.select_set(False)
            self.nb_qubits = 0
        else :
            self.nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))

        ####### SELECTED OBJECT #######

        row = self.addRow(1)
        row.label(text="Selected Object", icon="MESH_CUBE")
        row = self.addRow(1)
        row.prop(obj, "name")
        row.operator('object.select_object', text = '', icon="EYEDROPPER")
        #row.operator('object.select_object')
        
        row = self.addRow(5)
       
        ####### SETTINGS #######
        box = layout.box()
        
        box.label(text="Settings", icon="SETTINGS")
        row = self.addRow(3)

        ####### AXIS CHOICE #######

        box.label(text = "Axis", icon = 'ORIENTATION_LOCAL')
        row = self.addRow(1)
        row = layout.row()
        row = box.row()
        row.prop(context.scene.axis_choice, "axis", icon = 'ORIENTATION_LOCAL', expand = True)
        row = self.addRow(2)
            
        ####### QUBIT SELECTION #######

        box.label(text = "Select QuBit", icon = "LIGHTPROBE_GRID")
        index_qubit = bpy.types.Object.select_index
        box.operator('dialog.select_qubit', text = "ID = "+str(index_qubit), icon = "VIEWZOOM")
        row = self.addRow(3)
 
        ####### QUANTUM GATES #######
        
        box.label(text = "Quantum Gates", icon = 'SNAP_VERTEX')
        row = self.addRow(1)
        row = box.row()
        row.operator('object.add_and_del_gate', text='+').button = 'add'
        row.operator('object.add_and_del_gate', text='-').button = 'del'
        #row = self.addRow(3)

        ####### DISPLAY #######
        box = layout.box()
        if self.nb_qubits > 0:
            qindex = 0
            for qubit in DEMO_Manager.get_selected_circuit().data:
                qindex += 1
                gate_display = ""
                gate_display += "q" + str(qindex) + "  ---"
                for gate in qubit:
                    gate_display += "|" + gate.upper() + "|---"
                box.label(text=gate_display)
                row = self.addRow(1)

        else :                                        
            # bpy.context.active_object.select_set(False)
            # self.nb_qubits = 0
            box.label(text="Select a correct object")
            row = self.addRow(2)

        ####### THE END #######

        row.operator(ApplyQuantumCircuit.bl_idname, text="Apply", icon="CHECKMARK")
        row = self.addRow(1)
        row.operator(SwapToAn.bl_idname, text="Advanced (Quantum Magic)", icon="PLUS")

        #######################

def register():
    bpy.types.Scene.axis_choice = PointerProperty(type = SelectAxis)
    bpy.types.Scene.QuantumNodes_DEMO_Manager = QuantumNodes_DEMO_Manager()
    #bpy.types.Scene.ConfirmPopUpBis = ConfirmPopUp() 


if __name__ == "__main__":
    register()