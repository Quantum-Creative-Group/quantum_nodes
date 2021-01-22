import bpy

def genereateMultiplyAll(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"multiply_all")
    node_tree = bpy.data.node_groups[demo_id+"multiply_all"]
    node_tree_id = "_ma"

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_name = demo_id + "loop_in" + node_tree_id
    node_tree.nodes["Loop Input"].name = node_name
    loop_in = node_tree.nodes[node_name]
    loop_in.location[0] = -400
    loop_in.location[1] = -100
    loop_in.subprogramName = demo_id + "multiply_all"
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
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"max_values")
    node_tree = bpy.data.node_groups[demo_id+"max_values"]
    node_tree_id = "_mv"

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location[0] = -400
    grp_in.location[1] = -100
    grp_in.subprogramName = demo_id + "max_values"
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

def generateNegative(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"negative")
    node_tree = bpy.data.node_groups[demo_id+"negative"]
    node_tree_id = "_neg"

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_name = demo_id + "loop_in" + node_tree_id
    node_tree.nodes["Loop Input"].name = node_name
    loop_in = node_tree.nodes[node_name]
    loop_in.location[0] = -400
    loop_in.location[1] = -100
    loop_in.subprogramName = demo_id + "negative"
    loop_in.newIterator("Float List", "Float")

    # Loop output node (generator)
    node_tree.nodes.new(type = "an_LoopGeneratorOutputNode")
    node_name = demo_id + "loop_out" + node_tree_id
    node_tree.nodes["Loop Generator Output"].name = node_name
    loop_out = node_tree.nodes[node_name]
    loop_out.location[0] = 875
    loop_out.location[1] = -150
    loop_out.listDataType = "Float List"

    # Compare node
    node_tree.nodes.new(type="an_CompareNode")
    node_name = demo_id + "compare" + node_tree_id
    node_tree.nodes["Compare"].name = node_name
    compare = node_tree.nodes[node_name]
    compare.location[0] = 0
    compare.location[1] = -50
    compare.compareType = 'A>B'
    compare.inputs[1].value = 0.00

    # Switch node
    node_tree.nodes.new(type="an_SwitchNode")
    node_name = demo_id + "switch" + node_tree_id
    node_tree.nodes["Switch"].name = node_name
    switch = node_tree.nodes[node_name]
    switch.location[0] = 200
    switch.location[1] = -50
    switch.inputs[1].value = 1.00
    switch.inputs[2].value = -1.00

    # Linking everything
        # Loop in outputs to compare input
    node_tree.links.new(loop_in.outputs[2], compare.inputs[0])
        # Compare output to switch condition input
    node_tree.links.new(compare.outputs[0], switch.inputs[0])
        # Switch output to loop out input
    node_tree.links.new(switch.outputs[0], loop_out.inputs[0])

def generateMeshData(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"mesh_data")
    node_tree = bpy.data.node_groups[demo_id+"mesh_data"]
    node_tree_id = "_md"

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location[0] = -400
    grp_in.location[1] = -100
    grp_in.subprogramName = demo_id + "mesh_data"
    grp_in.newGroupInput("Float List", "Float List")
    grp_in.newGroupInput("Float List", "Float List")

    # Group output node
    node_tree.nodes.new(type="an_GroupOutputNode")
    node_name = demo_id + "grp_out" + node_tree_id
    node_tree.nodes["Group Output"].name = node_name
    grp_out = node_tree.nodes[node_name]
    grp_out.location[0] = 400
    grp_out.location[1] = -100
    grp_out.newGroupOutput("Float List", "Results")

    # Invoke multiply_all
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_multiply_all" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_mult_all = node_tree.nodes[node_name]
    inv_mult_all.location[0] = 200
    inv_mult_all.location[1] = 50
        # set subprogram
    inv_mult_all_inp = bpy.data.node_groups[demo_id+"multiply_all"].nodes[demo_id + "loop_in" + "_ma"]
    inv_mult_all.subprogramIdentifier = inv_mult_all_inp.identifier

    # Invoke negative
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_negative" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_neg = node_tree.nodes[node_name]
    inv_neg.location[0] = 300
    inv_neg.location[1] = 100
        # set subprogram
    inv_neg_inp = bpy.data.node_groups[demo_id+"negative"].nodes[demo_id + "loop_in" + "_neg"]
    inv_neg.subprogramIdentifier = inv_neg_inp.identifier

    # Invoke max_values
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_max_values" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_mv = node_tree.nodes[node_name]
    inv_mv.location[0] = -100
    inv_mv.location[1] = 100
        # set subprogram
    inv_mv_inp = bpy.data.node_groups[demo_id+"max_values"].nodes[demo_id + "grp_in" + "_mv"]
    inv_mv.subprogramIdentifier = inv_mv_inp.identifier

    # Multiply node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_multiply" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_mult = node_tree.nodes[node_name]
    math_mult.location[0] = 0
    math_mult.location[1] = -50
    math_mult.operation = 'MULTIPLY'

    # force to update socket inputs/outputs (tada !)
    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
    # Linking everything
        # Group in output
            # to invoke multiply_all
    node_tree.links.new(grp_in.outputs[0], inv_mult_all.inputs[0])
            # to invoke negative
    node_tree.links.new(grp_in.outputs[1], inv_neg.inputs[0])
            # to invoke max_values
    node_tree.links.new(grp_in.outputs[1], inv_mv.inputs[0])
        # Invoke negative output to invoke multiply_all input
    node_tree.links.new(inv_neg.outputs[0], inv_mult_all.inputs[1])
        # Invoke max_values output to math_mult input
    node_tree.links.new(inv_mv.outputs[0], math_mult.inputs[1])
        # Invoke multiply_all output to math_mult input
    node_tree.links.new(inv_mult_all.outputs[0], math_mult.inputs[0])
        # Math output to Group out input
    node_tree.links.new(math_mult.outputs[0], grp_out.inputs[0])

def generateMainNodeTree(context, demo_id):
    bpy.ops.node.new_node_tree(type="an_AnimationNodeTree", name=demo_id)
    node_tree = bpy.data.node_groups[demo_id]
    node_tree_id = "_main"

    # Mesh Object Input node
    node_tree.nodes.new(type="an_MeshObjectInputNode")
    node_name = demo_id + "mesh_obj_input" + node_tree_id
    node_tree.nodes["Mesh Object Input"].name = node_name
    mesh_obj_inp = node_tree.nodes[node_name]
    mesh_obj_inp.location[0] = -400
    mesh_obj_inp.location[1] = -100

    # Separate Vector node
    node_tree.nodes.new(type="an_SeparateVectorNode")
    node_name = demo_id + "sep_vecs" + node_tree_id
    node_tree.nodes["Separate Vector"].name = node_name
    sep_vecs = node_tree.nodes[node_name]
    sep_vecs.location[0] = -100
    sep_vecs.location[1] = -100

    inv_mesh_data_circuits = {"x" : None, "y" : None, "z" : None}
    for circ_name in ["x", "y", "z"]:
        # Invoke mesh_data_c(x/y/z)
        node_tree.nodes.new(type="an_InvokeSubprogramNode")
        node_name = demo_id + "invoke_mesh_data_" + circ_name + node_tree_id
        node_tree.nodes["Invoke Subprogram"].name = node_name
        inv_mesh_data_circuits[circ_name] = node_tree.nodes[node_name]
        inv_mesh_data_circuits[circ_name].location[0] = 200
        inv_mesh_data_circuits[circ_name].location[1] = 50
            # set subprogram
        subprog_inp = bpy.data.node_groups["an_q_demo_"+"mesh_data"].nodes["an_q_demo_" + "grp_in" + "_md"]
        inv_mesh_data_circuits[circ_name].subprogramIdentifier = subprog_inp.identifier

    # Combine Vector node
    node_tree.nodes.new(type="an_CombineVectorNode")
    node_name = demo_id + "comb_vecs" + node_tree_id
    node_tree.nodes["Combine Vector"].name = node_name
    comb_vecs = node_tree.nodes[node_name]
    comb_vecs.location[0] = 200
    comb_vecs.location[1] = -100

    # Mesh Object Output node
    node_tree.nodes.new(type="an_MeshObjectOutputNode")
    node_name = demo_id + "mesh_obj_output" + node_tree_id
    node_tree.nodes["Mesh Object Output"].name = node_name
    mesh_obj_out = node_tree.nodes[node_name]
    mesh_obj_out.location[0] = -400
    mesh_obj_out.location[1] = -100

    # force to update socket inputs/outputs (tada !)
    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
    # Linking everything
        # Invoke mesh_data_c(x/y/z) output to combine vector inputs
    for index, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        node_tree.links.new(inv_mesh_data_circuits[circ_name].outputs[0], comb_vecs.inputs[index])
    
