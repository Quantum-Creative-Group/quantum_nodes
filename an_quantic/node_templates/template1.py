import bpy
from animation_nodes.ui.node_menu import insertNode
from animation_nodes.utils.nodes import getAnimationNodeTrees


def templateInsertion(context, operator, custom_node_name):
    #bpy.ops.node.add_node(type="an_InvokeSubprogramNode", use_transform=True)
    QuGp = bpy.data.node_groups[custom_node_name]
    ####---NODES GENERATION---####
    bpy.data.node_groups[custom_node_name].nodes.new(type="an_LoopInputNode")
    QuGp.nodes["Loop Input"].name = "loop_in"
    QuGp.nodes["loop_in"].location[0] = -400
    QuGp.nodes["loop_in"].location[1] = -100
    QuGp.nodes["loop_in"].subprogramName = "Schrödinger"

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_SplitComplex128")
    QuGp.nodes["Split complex128"].name = "split_c"
    QuGp.nodes["split_c"].location[0] = -175
    QuGp.nodes["split_c"].location[1] = -150
    
    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    QuGp.nodes["Float Math"].name = "math_square_1"
    QuGp.nodes["math_square_1"].location[0] = 0
    QuGp.nodes["math_square_1"].location[1] = -50
    QuGp.nodes["math_square_1"].operation = 'POWER'
    QuGp.nodes["math_square_1"].inputs[1].value = 2

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    QuGp.nodes["Float Math"].name = "math_square_2"
    QuGp.nodes["math_square_2"].location[0] = 0
    QuGp.nodes["math_square_2"].location[1] = -200
    QuGp.nodes["math_square_2"].operation = 'POWER'
    QuGp.nodes["math_square_2"].inputs[1].value = 2        

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    QuGp.nodes["Float Math"].name = "math_add"
    QuGp.nodes["math_add"].location[0] = 175
    QuGp.nodes["math_add"].location[1] = -150
    QuGp.nodes["math_add"].operation = 'ADD'

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    QuGp.nodes["Float Math"].name = "math_square_root"
    QuGp.nodes["math_square_root"].location[0] = 350
    QuGp.nodes["math_square_root"].location[1] = -150
    QuGp.nodes["math_square_root"].operation = 'SQUARE_ROOT'

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_FloatMathNode")
    QuGp.nodes["Float Math"].name = "math_mult"
    QuGp.nodes["math_mult"].location[0] = 525
    QuGp.nodes["math_mult"].location[1] = -150
    QuGp.nodes["math_mult"].operation = 'MULTIPLY'
    QuGp.nodes["math_mult"].inputs[1].value = 20

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_CombineVectorNode")
    QuGp.nodes["Combine Vector"].name = "combine_vec"
    QuGp.nodes["combine_vec"].inputs[0].value = 0
    QuGp.nodes["combine_vec"].inputs[1].value = 0
    QuGp.nodes["combine_vec"].location[0] = 700
    QuGp.nodes["combine_vec"].location[1] = -150
    
    bpy.data.node_groups[custom_node_name].nodes.new(type = "an_LoopGeneratorOutputNode")
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

    bpy.data.node_groups[custom_node_name].nodes.new(type="an_InvokeSubprogramNode")
    QuGp.nodes["Invoke Subprogram"].name = "invoke_subpgm_schr"
    QuGp.nodes['invoke_subpgm_schr'].location[0] = 175
    QuGp.nodes['invoke_subpgm_schr'].location[0] = 500

    return 'lol'