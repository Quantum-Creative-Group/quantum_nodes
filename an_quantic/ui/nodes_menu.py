import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees

class QuanticExtensionMenu(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_extension_menu"
    bl_label = "Quantic Extension Menu"
    
    def draw(self, context):
        layout = self.layout
        # REPLACE with bl_idname and bl_label of the node in the nodes folder
        insertNode(layout, "an_MeshToHeight", "Mesh to Height")
        insertNode(layout, "an_HeightToMesh", "Height to Mesh")
        insertNode(layout, "an_HeightmapToQuantumCircuitNode", "Heightmap To Quantum Circuit")
        insertNode(layout, "an_QuantumCircuitToHeightmapNode", "Quantum Circuit To Heightmap")
        insertNode(layout, "an_InitClassicalRegisterNode", "Init Classical Register")
        insertNode(layout, "an_InitQuantumRegisterNode", "Init Quantum Register")
        #insertNode(layout, "an_InitQuantumCircuitNode", "Init Quantum Circuit")
        insertNode(layout, "an_QuantumGateHToAllNode", "Quantum GateH To All Circuit")
        insertNode(layout, "an_QuantumGateXToAllNode", "Quantum GateX To All Circuit")
        insertNode(layout, "an_QuantumGateYToAllNode", "Quantum GateY To All Circuit")
        insertNode(layout, "an_QuantumCircuitOutputStateNode", "Quantum Circuit Output State")
        insertNode(layout, "an_SchrodingerEquationSimulation", "Schrödinger Equation Simulation")

        insertNode(layout, "an_SplitComplex128", "Split complex128")
        layout.menu("AN_MT_quantic_gates", text = "Gates", icon = "SCRIPTPLUGINS")
        layout.separator()
        layout.menu("AN_MT_quantic_converters", text = "Converters", icon = "SCRIPTPLUGINS")
        layout.menu("AN_MT_quantic_complex", text = "Complex", icon = "SCRIPTPLUGINS")
        layout.menu("AN_MT_quantic_Qiskit", text = "Qiskit", icon = "SCRIPTPLUGINS")


class QuanticExtensionMenu_Gates(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_gates"
    bl_label = "Gates"
    
    def draw(self, context):
        layout = self.layout

class QuanticExtensionMenu_Converters(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_converters"
    bl_label = "Converters"
    
    def draw(self, context):
        layout = self.layout

class QuanticExtensionMenu_Complex(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_complex"
    bl_label = "Complex"
    
    def draw(self, context):
        layout = self.layout

class QuanticExtensionMenu_Qiskit(bpy.types.Menu):
    bl_idname = "AN_MT_quantic_Qiskit"
    bl_label = "Qiskit"
    
    def draw(self, context):
        layout = self.layout
        
       

class Pie_menu(bpy.types.Menu):
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
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if len(getAnimationNodeTrees()) == 0: return

    layout.separator()
    layout.menu("AN_MT_quantic_extension_menu", text = "Quantic Extension Menu", icon = "SCRIPTPLUGINS")

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)