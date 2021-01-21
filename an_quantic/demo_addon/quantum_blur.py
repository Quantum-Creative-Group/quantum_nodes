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
)
from bpy.types import(
    Panel,
    Operator,
    AddonPreferences,
    PropertyGroup,
)

class h_gate(bpy.types.Operator):
    bl_idname = "object.first_one_id"
    bl_label = "H - Gate"

    def execute(self, context):
        #DEMO_Manager.get_selected_circuit().add_gate(settings.nb_qubit-1, 'h')
        return{'FINISHED'}

class x_gate(bpy.types.Operator):
    bl_idname = "object.second_one_id"
    bl_label = "X - Gate"

    def execute(self, context):

        return{'FINISHED'}

class y_gate(bpy.types.Operator):
    bl_idname = "object.third_one_id"
    bl_label = "Y - Gate"

    def execute(self, context):

        return{'FINISHED'}

def draw_func(self, context):
    layout = self.layout

    layout.operator("object.first_one_id")
    layout.operator("object.second_one_id")
    layout.operator("object.third_one_id")

#class SimpleOperator(bpy.types.Operator):
#    bl_idname = "object.simple_operator"
#    bl_label = "Simple Object Operator"

#    @classmethod
#    def poll(cls, context):
#        return context.object is not None

#    def execute(self, context):
#        wm = bpy.context.window_manager
#        wm.popup_menu(draw_func, title="Options")
#        return {'FINISHED'}



class settings(PropertyGroup):

    x_tick: BoolProperty(
        name = "Enable x value",
        description = "Allows the algorithm to include the x value of the coordinate",
        default = False
    )
    y_tick: BoolProperty(
        name = "Enable y value",
        description = "Allows the algorithm to include the y value of the coordinate",
        default = False
    )
    z_tick: BoolProperty(
        name = "Enable z value",
        description = "Allows the algorithm to include the z value of the coordinate",
        default = False
    )
    h_gate_tick: BoolProperty(
        name = "Enable Hadamard gate",
        description = "Allows the algorithm to apply the Hadamard gate",
        default = True
    )
    x_gate_tick: BoolProperty(
        name = "Enable X gate",
        description = "Allows the algorithm to apply the X gate",
        default = False
    )
    y_gate_tick: BoolProperty(
        name = "Enable Y gate",
        description = "Allows the algorithm to apply the Y gate",
        default = False
    )
    nb_qubit : bpy.props.IntProperty(
        name = "Select",
        description = "Select a qubit",
        default = 1,
        min = 1,
        max = 10
    )

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
        settings = scene.quantumize_settings
        
        obj = context.object
        me = obj.data
        nb_vertices = (len(me.vertices))
        n = int(math.ceil(math.log(nb_vertices)/math.log(2)))
        print("nb of vertices = " + str(nb_vertices) + " ||||| nb of qubits = " + str(n))
            
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
        settings = context.scene.quantumize_settings
        DEMO_Manager = bpy.types.Scene.QuantumNodes_DEMO_Manager
        if self.button == 'add':
            wm = bpy.context.window_manager
            wm.popup_menu(draw_func, title="Options")
            DEMO_Manager.get_selected_circuit().add_gate(settings.nb_qubit-1, 'h') ######################### 'h' à modifier
        if self.button == 'del': 
            DEMO_Manager.get_selected_circuit().del_gate(settings.nb_qubit-1)
        return{'FINISHED'}

class quantumize_ui(bpy.types.Panel):
    bl_label = "Quantumize"
    bl_idname = "quantumize_op"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QuantumMesh"

        
    
    def draw(self, context):
        # variables
        layout = self.layout
        scene = context.scene
        obj = bpy.context.active_object
        settings = scene.quantumize_settings

     
        #if obj.name != self.obj_tmp: self.obj_tmp = obj.name

        nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))

        #update selected circuit
        bpy.types.Scene.QuantumNodes_DEMO_Manager.selected_circuit = context.scene.axis_choice.axis 
        #print(bpy.types.Scene.QuantumNodes_DEMO_Manager.selected_circuit)

        if nb_qubits > 10 or bpy.context.active_object == False: 
            bpy.context.active_object.select_set(False)
            nb_qubits = 0

        row = layout.row()
        row.label(text="Objet sélectionné", icon="MESH_CUBE")
        row = layout.row()
        row.prop(obj, "name")
        for i in range(5) : row = layout.row()
        row.label(text="Paramètres", icon="SETTINGS")
        for i in range(3) : row = layout.row()
        row.label(text = "Axis", icon = 'ORIENTATION_LOCAL')
        row = layout.row()
        row.prop(context.scene.axis_choice, "axis", icon = 'ORIENTATION_LOCAL', expand = True)
        for i in range(2) : row = layout.row()
        row.label(text = "ID Qbit", icon = "LIGHTPROBE_GRID")
        row.prop(settings, "nb_qubit")
        for i in range(3) : row = layout.row()
        row.label(text = "Quantum Gates", icon = 'SNAP_VERTEX')
        row = layout.row()
        layout.operator('object.add_and_del_gate', text='+').button = 'add'
        layout.operator('object.add_and_del_gate', text='-').button = 'del'
        #row.prop(settings, "h_gate_tick", text = "H gate")
        #row.prop(settings, "x_gate_tick", text = "X gate")
        #row.prop(settings, "y_gate_tick", text = "Y gate")
        for i in range(3) : row = layout.row()
        for i in range(nb_qubits):
            gate_display = ""
            if settings.h_gate_tick : gate_display += "---|H|---"
            if settings.x_gate_tick : gate_display += "---|X|---"
            if settings.y_gate_tick : gate_display += "---|Y|---"  
            row.label(text="q"+str(i)+gate_display)
            row = layout.row()
        for i in range(2) : row = layout.row()
        for i in range(2) : row = layout.row()
        row.operator(quantumize_op.bl_idname, text="Appliquer", icon="CHECKMARK")
        row = layout.row()
        row.operator(swap_to_an.bl_idname, text="Advanced", icon="PLUS")

classes = (
    settings,
    SelectAxis,
    AddAndDelGate,
    quantumize_op,
    quantumize_ui,
)

def register():
    bpy.types.Scene.quantumize_settings = PointerProperty(type = settings)
    bpy.types.Scene.axis_choice = PointerProperty(type = SelectAxis)
    bpy.types.Scene.QuantumNodes_DEMO_Manager = QuantumNodes_DEMO_Manager()


if __name__ == "__main__":
    register()


