import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees



class InsertNodeUI(bpy.types.Panel):
    bl_label = "Quantum Node Panel"
    bl_idname = "InsertNodeUI"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "QuantumNode"


    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator('nodes.insert', text='Insert new node Tree')

def create_quantum_node_tree(context, operator, gp_name):
    bpy.context.scene.use_nodes = True #use nodes activated
    
    QuantumTree = bpy.ops.node.new_node_tree(name=gp_name)
    
    return QuantumTree


class InsertNodeOP(bpy.types.Operator):
    bl_idname = "nodes.insert"
    bl_label = "Add Quantum Node Tree"

    def execute(self, context):
        custom_node_name = "Quantum_Node_Tree"

        ####---NODES TREE GENERATION---####
        create_quantum_node_tree(context, self, custom_node_name)

        QuGp = bpy.data.node_groups["Quantum_Node_Tree"]
     
        ####---NODES GENERATION---####
        bpy.ops.node.add_node(type="an_LoopInputNode", use_transform=True)
        QuGp.nodes["Loop Input"].name = "loop_in"
        QuGp.nodes["loop_in"].location[0] = -400
        QuGp.nodes["loop_in"].location[1] = -100
        QuGp.nodes["loop_in"].subprogramName = "Schrödinger"

        bpy.ops.node.add_node(type="an_SplitComplex128", use_transform=True)
        QuGp.nodes["Split complex128"].name = "split_c"
        QuGp.nodes["split_c"].location[0] = -175
        QuGp.nodes["split_c"].location[1] = -150
        
        bpy.ops.node.add_node(type="an_FloatMathNode", use_transform=True)
        QuGp.nodes["Float Math"].name = "math_square_1"
        QuGp.nodes["math_square_1"].location[0] = 0
        QuGp.nodes["math_square_1"].location[1] = -50
        QuGp.nodes["math_square_1"].operation = 'POWER'
        QuGp.nodes["math_square_1"].inputs[1].value = 2
      
        bpy.ops.node.add_node(type="an_FloatMathNode", use_transform=True)
        QuGp.nodes["Float Math"].name = "math_square_2"
        QuGp.nodes["math_square_2"].location[0] = 0
        QuGp.nodes["math_square_2"].location[1] = -200
        QuGp.nodes["math_square_2"].operation = 'POWER'
        QuGp.nodes["math_square_2"].inputs[1].value = 2        

        bpy.ops.node.add_node(type="an_FloatMathNode", use_transform=True)
        QuGp.nodes["Float Math"].name = "math_add"
        QuGp.nodes["math_add"].location[0] = 175
        QuGp.nodes["math_add"].location[1] = -150
        QuGp.nodes["math_add"].operation = 'ADD'

        bpy.ops.node.add_node(type="an_FloatMathNode", use_transform=True)
        QuGp.nodes["Float Math"].name = "math_square_root"
        QuGp.nodes["math_square_root"].location[0] = 350
        QuGp.nodes["math_square_root"].location[1] = -150
        QuGp.nodes["math_square_root"].operation = 'SQUARE_ROOT'

        bpy.ops.node.add_node(type="an_FloatMathNode", use_transform=True)
        QuGp.nodes["Float Math"].name = "math_mult"
        QuGp.nodes["math_mult"].location[0] = 525
        QuGp.nodes["math_mult"].location[1] = -150
        QuGp.nodes["math_mult"].operation = 'MULTIPLY'
        QuGp.nodes["math_mult"].inputs[1].value = 20

        bpy.ops.node.add_node(type="an_CombineVectorNode", use_transform=True)
        QuGp.nodes["Combine Vector"].name = "combine_vec"
        QuGp.nodes["combine_vec"].inputs[0].value = 0
        QuGp.nodes["combine_vec"].inputs[1].value = 0
        QuGp.nodes["combine_vec"].location[0] = 700
        QuGp.nodes["combine_vec"].location[1] = -150
        
        bpy.ops.node.add_and_link_node(type = "an_LoopGeneratorOutputNode", use_transform=True)
        QuGp.nodes["Loop Generator Output"].name = "loop_out"
        QuGp.nodes["loop_out"].location[0] = 875
        QuGp.nodes["loop_out"].location[1] = -150
        
        ####---LINKS---####
        QuGp.links.new(QuGp.nodes["loop_in"].outputs[2], QuGp.nodes["split_c"].inputs[0])
        QuGp.links.new(QuGp.nodes["split_c"].outputs[0], QuGp.nodes["math_square_1"].inputs[0])
        QuGp.links.new(QuGp.nodes["split_c"].outputs[1], QuGp.nodes["math_square_2"].inputs[0])
        QuGp.links.new(QuGp.nodes["math_square_1"].outputs[0], QuGp.nodes["math_add"].inputs[0])
        QuGp.links.new(QuGp.nodes["math_square_2"].outputs[0], QuGp.nodes["math_add"].inputs[1])

        QuGp.links.new(QuGp.nodes["math_add"].outputs[0], QuGp.nodes["math_square_root"].inputs[0])
        QuGp.links.new(QuGp.nodes["math_square_root"].outputs[0], QuGp.nodes["math_mult"].inputs[0])
        QuGp.links.new(QuGp.nodes["math_mult"].outputs[0], QuGp.nodes["combine_vec"].inputs[2])
        QuGp.links.new(QuGp.nodes["combine_vec"].outputs[0], QuGp.nodes["loop_out"].inputs[0])
        
        return {'FINISHED'}

#def insertNode(context, operator, node_name):

#def register():
    #bpy.types.NODE_MT_add.append(drawMenu)

#def unregister():
    #bpy.types.NODE_MT_add.remove(drawMenu)