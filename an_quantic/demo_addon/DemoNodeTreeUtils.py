import bpy

def genereateMultiplyAll(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name="multiply_all")
    node_tree = bpy.data.node_groups["multiply_all"]

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_tree.nodes["Loop Input"].name = demo_id + "loop_in"
    loop_in = node_tree.nodes[demo_id + "loop_in"]
    loop_in.location[0] = -400
    loop_in.location[1] = -100
    loop_in.subprogramName = "multiply_all"
    loop_in.newIterator("Float List", "Float")
    loop_in.newIterator("Float List", "Float")

    # Loop output node (generator)
    node_tree.nodes.new(type = "an_LoopGeneratorOutputNode")
    node_tree.nodes["Loop Generator Output"].name = demo_id + "loop_out"
    loop_out = node_tree.nodes[demo_id + "loop_out"]
    loop_out.location[0] = 875
    loop_out.location[1] = -150
    loop_out.listDataType = "Float List"

    # Multiply node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_tree.nodes["Float Math"].name = demo_id + "math_multiply"
    math_mult = node_tree.nodes[demo_id + "math_multiply"]
    math_mult.location[0] = 0
    math_mult.location[1] = -50
    math_mult.operation = 'MULTIPLY'

    # Linking everything
        # Loop in outputs to math inputs
    node_tree.links.new(loop_in.outputs[2], math_mult.inputs[0])
    node_tree.links.new(loop_in.outputs[3], math_mult.inputs[1])
        # Math output to loop out input
    node_tree.links.new(math_mult.outputs[0], loop_out.inputs[0])

def generateMaxValue(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name="max_value")
    node_tree = bpy.data.node_groups["multiply_all"]

    # Group input node
    

