import math
import bpy, os, sys

from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager
from .. operators.SwitchToAn import SwitchToAn
from .. properties.SelectAxis import SelectAxis
from .. operators.AddGateButton import AddGateButton
from .. operators.AddAndDelGate import AddAndDelGate
from .. operators.SelectQubit import SelectQubit
from .. operators.ApplyQuantumCircuit import ApplyQuantumCircuit

from bpy.props import PointerProperty
from bpy.types import Panel

class AN_Q_DemoAddon(bpy.types.Panel):
    bl_idname = "AN_Q_PT_addon_demo_ui"
    bl_label = "AN_Q Demo addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AN_Q_DEMO"

    bpy.types.Object.select_index = 0
  
    def addRow(self, n):
        for i in range(n): row = self.layout.row()
        return row
    
    def draw(self, context):
        # ---------- Initialization ----------

        layout = self.layout
        DEMO_Manager = bpy.types.Scene.demo_manager

        if DEMO_Manager.selected_obj == None:
            # initializes the first circuit with the default cube 
            DEMO_Manager.createNewCircuit(bpy.context.active_object)

        obj = DEMO_Manager.selected_obj

        # ---------- Updates selected circuit ----------

        DEMO_Manager.selected_circuit = context.scene.selected_axis.axis

        # ---------- Object selection ----------

        row = self.addRow(1)
        row.label(text="Target", icon="MESH_CUBE")
        row = self.addRow(1)
        row.prop(obj, "name")
        row.operator('object.select_object', text = '', icon="EYEDROPPER")
        row = self.addRow(1)
       
        # ---------- Settings section ----------

        box = layout.box()
        box.label(text="Settings", icon="SETTINGS")

            # ---------- Axis selection ----------

        box.label(text = "Axis", icon = 'ORIENTATION_LOCAL')
        row = box.row()
        row.prop(context.scene.selected_axis, "axis", icon = 'ORIENTATION_LOCAL', expand = True)
        row = self.addRow(1)

            # ---------- Qubit selection ----------

        box.label(text = "Select QuBit", icon = "LIGHTPROBE_GRID")
        box.operator('dialog.select_qubit', text = "q"+str(bpy.types.Object.select_index + 1), icon = "VIEWZOOM")
 
            # ---------- Gate selection ----------
        
        box.label(text = "Quantum Gates", icon = 'SNAP_VERTEX')
        row = box.row()
        row.operator('object.add_and_del_gate', text='+').button = 'add'
        row.operator('object.add_and_del_gate', text='-').button = 'del'

        # ---------- Circuit display ----------
        box = layout.box()
        if DEMO_Manager.nb_qubits > 0:
            qindex = 0
            for qubit in DEMO_Manager.get_selected_circuit().data:
                qindex += 1
                gate_display = ""
                gate_display += "q" + str(qindex) + "  ---"
                for gate in qubit:
                    gate_display += "|" + gate.upper() + "|---"
                box.label(text=gate_display)

        else :                                        
            box.label(text="Select a correct object")

        # ---------- End buttons ----------

        row = self.addRow(2)
        row.operator(ApplyQuantumCircuit.bl_idname, text="Apply", icon="CHECKMARK")
        row = self.addRow(1)
        row.operator(SwitchToAn.bl_idname, text="Advanced (Quantum Magic)", icon="PLUS")

def register():
    # PointerProperty : https://docs.blender.org/api/current/bpy.props.html
    # (it is possible to set a poll function if needed for selected_axis)
    bpy.types.Scene.selected_axis = PointerProperty(type = SelectAxis)
    bpy.types.Scene.demo_manager = QuantumNodes_DEMO_Manager()

if __name__ == "__main__":
    register()