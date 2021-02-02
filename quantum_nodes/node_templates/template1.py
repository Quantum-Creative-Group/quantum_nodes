import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees


def templateInsertion(context, operator, custom_node_name):
    node_tree = bpy.data.node_groups[custom_node_name]
    # ---------- NODES GENERATION ----------
    bpy.data.node_groups[custom_node_name].nodes.new(type="an_LoopInputNode")
    node_tree.nodes["Loop Input"].name = "loop_in"
    node_tree.nodes["loop_in"].location[0] = -400
    node_tree.nodes["loop_in"].location[1] = -100
    node_tree.nodes["loop_in"].subprogramName = "Schrödinger"

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_SplitComplex128")
    node_tree.nodes["Split complex128"].name = "split_c"
    node_tree.nodes["split_c"].location[0] = -175
    node_tree.nodes["split_c"].location[1] = -150
    
    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = "math_square_1"
    node_tree.nodes["math_square_1"].location[0] = 0
    node_tree.nodes["math_square_1"].location[1] = -50
    node_tree.nodes["math_square_1"].operation = 'POWER'
    node_tree.nodes["math_square_1"].inputs[1].value = 2

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = "math_square_2"
    node_tree.nodes["math_square_2"].location[0] = 0
    node_tree.nodes["math_square_2"].location[1] = -200
    node_tree.nodes["math_square_2"].operation = 'POWER'
    node_tree.nodes["math_square_2"].inputs[1].value = 2        

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = "math_add"
    node_tree.nodes["math_add"].location[0] = 175
    node_tree.nodes["math_add"].location[1] = -150
    node_tree.nodes["math_add"].operation = 'ADD'

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = "math_square_root"
    node_tree.nodes["math_square_root"].location[0] = 350
    node_tree.nodes["math_square_root"].location[1] = -150
    node_tree.nodes["math_square_root"].operation = 'SQUARE_ROOT'

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = "math_mult"
    node_tree.nodes["math_mult"].location[0] = 525
    node_tree.nodes["math_mult"].location[1] = -150
    node_tree.nodes["math_mult"].operation = 'MULTIPLY'
    node_tree.nodes["math_mult"].inputs[1].value = 20

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_CombineVectorNode")
    node_tree.nodes["Combine Vector"].name = "combine_vec"
    node_tree.nodes["combine_vec"].inputs[0].value = 0
    node_tree.nodes["combine_vec"].inputs[1].value = 0
    node_tree.nodes["combine_vec"].location[0] = 700
    node_tree.nodes["combine_vec"].location[1] = -150
    
    bpy.data.node_groups[custom_node_name].nodes.new(type = "an_LoopGeneratorOutputNode")
    node_tree.nodes["Loop Generator Output"].name = "loop_out"
    node_tree.nodes["loop_out"].location[0] = 875
    node_tree.nodes["loop_out"].location[1] = -150
        # ---------- LINKS ----------
    node_tree.links.new(node_tree.nodes["loop_in"].outputs[2], node_tree.nodes["split_c"].inputs[0])
    node_tree.links.new(node_tree.nodes["split_c"].outputs[0], node_tree.nodes["math_square_1"].inputs[0])
    node_tree.links.new(node_tree.nodes["split_c"].outputs[1], node_tree.nodes["math_square_2"].inputs[0])
    node_tree.links.new(node_tree.nodes["math_square_1"].outputs[0], node_tree.nodes["math_add"].inputs[0])
    node_tree.links.new(node_tree.nodes["math_square_2"].outputs[0], node_tree.nodes["math_add"].inputs[1])

    node_tree.links.new(node_tree.nodes["math_add"].outputs[0], node_tree.nodes["math_square_root"].inputs[0])
    node_tree.links.new(node_tree.nodes["math_square_root"].outputs[0], node_tree.nodes["math_mult"].inputs[0])
    node_tree.links.new(node_tree.nodes["math_mult"].outputs[0], node_tree.nodes["combine_vec"].inputs[2])
    node_tree.links.new(node_tree.nodes["combine_vec"].outputs[0], node_tree.nodes["loop_out"].inputs[0])

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_InvokeSubprogramNode")
    node_tree.nodes["Invoke Subprogram"].name = "invoke_subpgm_schr"
    node_tree.nodes['invoke_subpgm_schr'].location[0] = 175
    node_tree.nodes['invoke_subpgm_schr'].location[0] = 500