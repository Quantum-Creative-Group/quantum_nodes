import math
import bpy, os, sys

from .. backend.QuantumNodes_DEMO_Manager import QuantumNodes_DEMO_Manager
from .. operators.SwitchToAn import SwitchToAn
from .. properties.SelectAxis import SelectAxis
from .. operators.AddGateButton import AddGateButton
from .. operators.AddAndDelGate import AddAndDelGate
from .. operators.SelectQubit import SelectQubit
from .. operators.ApplyQuantumCircuit import ApplyQuantumCircuit
from .. operators.ResetCircuits import ResetCircuits
from .. operators.DeleteTarget import DeleteTarget

from bpy.props import PointerProperty
from bpy.types import Panel

# TODO: find a way to allow undo for the addon
# def undo_addon_handler(scene):
#     dm = scene.demo_manager
#     print(dm)

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
        dm = bpy.types.Scene.demo_manager
        obj = dm.target

        # ---------- Updates selected circuit ----------

        dm.selected_circuit = context.scene.selected_axis.axis

        # ---------- Object selection ----------

        row = self.addRow(1)
        row.label(text="Target", icon="MESH_CUBE")
        row = self.addRow(1)

        # These two lines causes a crash on undo (invalid object) (segfault)
        # TODO: find a solution for this bug
        # if(obj != None): row.prop(obj, "name")
        # else: row.label(text="Select a target")

        row.operator('object.delete_target', text = '', icon="CANCEL")
        row.operator('object.select_object', text = '', icon="EYEDROPPER")
        row = self.addRow(1)
       
        # ---------- Settings section ----------

        if obj != None:
            box = layout.box()
            box.label(text="Settings", icon="SETTINGS")

            # ---------- Axis selection ----------

            box.label(text = "Axis", icon = 'ORIENTATION_LOCAL')
            row = box.row()
            row.prop(context.scene.selected_axis, "axis", icon = 'ORIENTATION_LOCAL', expand = True)
            row = self.addRow(1)

            # ---------- Qubit selection ----------

            box.label(text = "Select QuBit", icon = "LIGHTPROBE_GRID")
            box.operator('dialog.select_qubit', text = "q" + str(bpy.types.Object.select_index + 1), icon = "VIEWZOOM")
 
            # ---------- Gate selection ----------
        
            box.label(text = "Quantum Gates", icon = 'SNAP_VERTEX')
            row = box.row()
            row.operator('object.add_and_del_gate', text='+').button = 'add'
            row.operator('object.add_and_del_gate', text='-').button = 'del'

            # ---------- Circuit display ----------
            box = layout.box()
            if dm.nb_qubits > 0:
                qindex = 0
                for qubit in dm.getSelectedCircuit().data:
                    qindex += 1
                    gate_display = ""
                    gate_display += "q" + str(qindex) + "  ---"
                    for gate in qubit:
                        gate_display += "|" + gate.upper() + "|---"
                    box.label(text=gate_display)

            else :                                        
                box.label(text="Select a correct object")
            
            row = box.row()
            row.operator("object.reset_quantum_circuits", text = "Reset circuits", icon="RECOVER_LAST")

            # ---------- End buttons ----------

            row = self.addRow(2)
            row.operator(ApplyQuantumCircuit.bl_idname, text = "Apply", icon = "CHECKMARK")
            row.operator("object.duplicate_target", text = "Duplicate", icon = "DUPLICATE")
            row = self.addRow(1)
            row.operator(SwitchToAn.bl_idname, text = "Advanced (Quantum Magic)", icon = "PLUS")
            row = self.addRow(4)

            row.operator('wm.url_open', text = "Need Help ?", icon = 'BOOKMARKS').url = 'https://elgoog.im/'
            row = self.addRow(1)
            row.operator('wm.url_open', text = "Creation gallery", icon = 'FUND').url = 'https://www.instagram.com/theo_goatyeah'

def register():
    # PointerProperty : https://docs.blender.org/api/current/bpy.props.html
    # (it is possible to set a poll function if needed for selected_axis)
    bpy.types.Scene.selected_axis = PointerProperty(type = SelectAxis)
    bpy.types.Scene.demo_manager = QuantumNodes_DEMO_Manager()
    # bpy.app.handlers.undo_pre.append(undo_addon_handler)

if __name__ == "__main__":
    register()