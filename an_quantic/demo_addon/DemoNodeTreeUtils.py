import bpy

def genereateMultiplyAll(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name="multiply_all")
    node_tree = bpy.data.node_groups["multiply_all"]
    node_tree_id = "_ma"

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_name = demo_id + "loop_in" + node_tree_id
    node_tree.nodes["Loop Input"].name = node_name
    loop_in = node_tree.nodes[node_name]
    loop_in.location[0] = -400
    loop_in.location[1] = -100
    loop_in.subprogramName = "multiply_all"
    loop_in.newIterator("Float List", "Float")
    loop_in.newIterator("Float List", "Float")

    # Loop output node (generator)
    node_tree.nodes.new(type = "an_LoopGeneratorOutputNode")
    node_name = demo_id + "loop_out" + node_tree_id
    node_tree.nodes["Loop Generator Output"].name = node_name
    loop_out = node_tree.nodes[node_name]
    loop_out.location[0] = 875
    loop_out.location[1] = -150
    loop_out.listDataType = "Float List"

    # Multiply node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_multiply" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_mult = node_tree.nodes[node_name]
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
    node_tree = bpy.data.node_groups["max_value"]
    node_tree_id = "_mv"

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location[0] = -400
    grp_in.location[1] = -100
    grp_in.subprogramName = "max_value"
    grp_in.newGroupInput("Float List", "Float List")

    # Group output node
    node_tree.nodes.new(type="an_GroupOutputNode")
    node_name = demo_id + "grp_out" + node_tree_id
    node_tree.nodes["Group Output"].name = node_name
    grp_out = node_tree.nodes[node_name]
    grp_out.location[0] = 400
    grp_out.location[1] = -100
    grp_out.newGroupOutput("Float", "Result")

    # To absolute node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_abs" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_abs = node_tree.nodes[node_name]
    math_abs.location[0] = 0
    math_abs.location[1] = -50
    math_abs.operation = 'ABSOLUTE'

    # Max value node
    node_tree.nodes.new(type="an_NumberListMathNode")
    node_name = demo_id + "n_list_math" + node_tree_id
    print(node_tree.nodes[3])
    node_tree.nodes["Number List Math"].name = node_name
    n_list_math = node_tree.nodes[node_name]
    n_list_math.location[0] = 200
    n_list_math.location[1] = -50
    n_list_math.operation = 'MAX'

    # Linking everything
        # Group in output to math input
    node_tree.links.new(grp_in.outputs[0], math_abs.inputs[0])
        # Math output to Numer List Math
    node_tree.links.new(math_abs.outputs[0], n_list_math.inputs[0])
        # Number List Math output to Group out input
    node_tree.links.new(n_list_math.outputs[0], grp_out.inputs[0])
    

