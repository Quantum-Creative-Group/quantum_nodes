import bpy, os
import bpy.utils.previews

from typing import Optional

from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

class QuanticExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_extension_menu"
    bl_label = "Quantic Extension Menu"
    

    def draw(self, context):
        pcoll = preview_collections["main"]
        my_icon = pcoll["my_icon"]
        layout = self.layout
        # REPLACE with bl_idname and bl_label of the node in the nodes folder     
        layout.menu("AN_MT_quantic_gates", text = "Quantum Gates", icon = "SHADING_BBOX")
        layout.menu("AN_MT_quantic_complex", text = "Complex Numbers", icon = "MESH_UVSPHERE")
        layout.separator()
        layout.menu("AN_MT_quantic_qu_heightmap", text = "Quantum Heightmap", icon = "ORIENTATION_VIEW")
        layout.menu("AN_MT_quantic_init_qu_circuit", text = "Init Quantum Circuit", icon = "KEYINGSET")
        layout.menu("AN_MT_quantic_qu_output", text = "Quantum Output", icon = "ORIENTATION_NORMAL")
        layout.separator()
        layout.menu("AN_MT_quantic_schrodinger_simulation", text = "Schrödinger Simulation", icon = "OPTIONS")
        #layout.label(text='lol', icon_value=my_icon.icon_id)


################# MENU-CLASSES ################# 

class QuanticExtensionMenu_Complex(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_complex"
    bl_label = "Complex Numbers"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SplitComplex128", "Split complex128")

class QuanticExtensionMenu_Heightmap(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_qu_heightmap"
    bl_label = "Quantum Heightmap"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_MeshToHeight", "Mesh to Height")
        insertNode(layout, "an_HeightToMesh", "Height to Mesh")
        insertNode(layout, "an_QuantumCircuitToHeightmapNode", "Quantum Circuit To Heightmap")
        insertNode(layout, "an_HeightmapToQuantumCircuitNode", "Heightmap To Quantum Circuit")

class QuanticExtensionMenu_Circuit(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_init_qu_circuit"
    bl_label = "Init Quantum Circuit"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_InitClassicalRegisterNode", "Init Classical Register")
        insertNode(layout, "an_InitQuantumRegisterNode", "Init Quantum Register")
        insertNode(layout, "an_InitQuantumCircuitNode", "Init Quantum Circuit")

class QuanticExtensionMenu_Output(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_qu_output"
    bl_label = "Quantum Output"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumCircuitGetCountNode", "Quantum Circuit Get Count")
        insertNode(layout, "an_QuantumCircuitOutputStateNode", "Quantum Circuit Output State")
        insertNode(layout, "an_QuantumMeasureNode", "Quantum Measure")
        insertNode(layout, "an_QuantumCircuitIBMOutputStateNode", "Quantum Circuit IBM Output State")

class QuanticExtensionMenu_Schrodinger(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_schrodinger_simulation"
    bl_label = "Schrödinger Simulation"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_SchrodingerEquationSimulation", "Schrödinger Equation Simulation")

class QuanticExtensionMenu_Gates(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates"
    bl_label = "Gates"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCCXNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCSWAPNode", "Quantum Gate CSWAP")
        insertNode(layout, "an_QuantumGateSWAPNode", "Quantum Gate SWAP")
        layout.separator()
        layout.menu("AN_MT_quantic_gates_c", text = "Gates_C", icon = "EVENT_C")
        layout.menu("AN_MT_quantic_gates_r", text = "Gates_R", icon = "EVENT_R")
        layout.menu("AN_MT_quantic_gates_to_all", text = "Gates_To_All", icon = "OBJECT_ORIGIN")
        layout.menu("AN_MT_quantic_gates_single_qubit", text = "Single_Qubit_Gates", icon = "DOT")


################# GATES - SUBMENU ################# 

class QuanticExtensionMenu_Gates_c(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates_c"
    bl_label = "Gates_C"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCHNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCXNode", "Quantum Gate CX")
        insertNode(layout, "an_QuantumGateCYNode", "Quantum Gate CY")
        insertNode(layout, "an_QuantumGateCZNode", "Quantum Gate CZ")

class QuanticExtensionMenu_Gates_r(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates_r"
    bl_label = "Gates_R"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateRXNode", "Quantum Gate RX")
        insertNode(layout, "an_QuantumGateRYNode", "Quantum Gate RY")
        insertNode(layout, "an_QuantumGateRZNode", "Quantum Gate RZ")

class QuanticExtensionMenu_Gates_to_all(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates_to_all"
    bl_label = "Gates_To_All"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateHToAllNode", "Quantum Gate H To All Circuit")
        insertNode(layout, "an_QuantumGateIDToAllNode", "Quantum Gate ID To All Circuit")
        insertNode(layout, "an_QuantumGateSToAllNode", "Quantum Gate S To All Circuit")
        insertNode(layout, "an_QuantumGateSDGToAllNode", "Quantum Gate SDG To All Circuit")
        insertNode(layout, "an_QuantumGateTToAllNode", "Quantum Gate T To All Circuit")
        insertNode(layout, "an_QuantumGateTDGToAllNode", "Quantum Gate TDG To All Circuit")
        insertNode(layout, "an_QuantumGateXToAllNode", "Quantum Gate X To All Circuit")
        insertNode(layout, "an_QuantumGateYToAllNode", "Quantum Gate Y To All Circuit")
        insertNode(layout, "an_QuantumGateZToAllNode", "Quantum Gate Z To All Circuit")

class QuanticExtensionMenu_Gates_Single_Qubit(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates_single_qubit"
    bl_label = "Single_Qubit_Gates"
    
    def draw(self, context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateHNode", "Quantum Gate H")
        insertNode(layout, "an_QuantumGateIDNode", "Quantum Gate ID")
        insertNode(layout, "an_QuantumGateSNode", "Quantum Gate S")
        insertNode(layout, "an_QuantumGateSDGNode", "Quantum Gate SDG")
        insertNode(layout, "an_QuantumGateTNode", "Quantum Gate T")
        insertNode(layout, "an_QuantumGateTDGNode", "Quantum Gate TDG")
        insertNode(layout, "an_QuantumGateXNode", "Quantum Gate X")
        insertNode(layout, "an_QuantumGateYNode", "Quantum Gate Y")
        insertNode(layout, "an_QuantumGateZNode", "Quantum Gate Z")
  



################# PIE MENU : A DEVELOPPER ################# 

class Pie_menu(bpy.types.Menu):
    bl_idname = "AN_MT_pie_menu"
    bl_label = "Some Pie Menu"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("wm.call_menu_pie", text = "Some Other Pie", icon = "RIGHTARROW_THIN").name="Pie_menu"
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.operator("mesh.primitive_cube_add", text = "Some Operator", icon = "BLENDER")
        pie.separator()
        pie.separator()
        other = pie.column()
        gap = other.column()
        gap.separator()
        gap.scale_y = 7
        other_menu = other.box().column()
        other_menu.scale_y=1.3
        other_menu.operator("mesh.primitive_cube_add", text = "Some Menu Operator",icon = "BLENDER")
        other_menu.operator("mesh.primitive_cube_add", text = "Some Menu Operator",icon = "BLENDER") 
        other_menu.menu('Submenu', icon='RIGHTARROW_THIN',  text='Some Submenu...')


def drawMenu(self, context):
    pcoll = preview_collections["main"]
    my_icon = pcoll["my_icon"]
    
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0: return

    layout.separator()
    layout.menu("AN_MT_quantic_extension_menu", text = "Quantic Extension Menu", icon_value=my_icon.icon_id)

preview_collections = {}

def register():
    import bpy, os
    bpy.types.NODE_MT_add.append(drawMenu)

    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "discord.png"), 'IMAGE')

    preview_collections["main"] = pcoll

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()