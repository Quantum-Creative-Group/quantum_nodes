import bpy

def genereateMultiplyAll(context, demo_id):
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"multiply_all")
    node_tree = bpy.data.node_groups[demo_id+"multiply_all"]
    node_tree_id = "_ma"

    # auto-execution parameters
    node_tree.autoExecution.enabled = False

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_name = demo_id + "loop_in" + node_tree_id
    node_tree.nodes["Loop Input"].name = node_name
    loop_in = node_tree.nodes[node_name]
    loop_in.location = (0, 0)
    loop_in.subprogramName = demo_id + "multiply_all"
    loop_in.newIterator("Float List", "Float")
    loop_in.newIterator("Float List", "Float")

    # Loop output node (generator)
    node_tree.nodes.new(type = "an_LoopGeneratorOutputNode")
    node_name = demo_id + "loop_out" + node_tree_id
    node_tree.nodes["Loop Generator Output"].name = node_name
    loop_out = node_tree.nodes[node_name]
    loop_out.location = (425, 0)
    loop_out.listDataType = "Float List"

    # Multiply node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_multiply" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_mult = node_tree.nodes[node_name]
    math_mult.location = (225, 0)
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

    # auto-execution parameters
    node_tree.autoExecution.enabled = False

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location = (0, 0)
    grp_in.subprogramName = demo_id + "max_values"
    grp_in.newGroupInput("Float List", "Float List")

    # Group output node
    node_tree.nodes.new(type="an_GroupOutputNode")
    node_name = demo_id + "grp_out" + node_tree_id
    node_tree.nodes["Group Output"].name = node_name
    grp_out = node_tree.nodes[node_name]
    grp_out.location = (600, 0)
    grp_out.newGroupOutput("Float", "Result")

    # To absolute node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_abs" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_abs = node_tree.nodes[node_name]
    math_abs.location = (225, 0)
    math_abs.operation = 'ABSOLUTE'

    # Max value node
    node_tree.nodes.new(type="an_NumberListMathNode")
    node_name = demo_id + "n_list_math" + node_tree_id
    node_tree.nodes["Number List Math"].name = node_name
    n_list_math = node_tree.nodes[node_name]
    n_list_math.location = (410, 0)
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

    # auto-execution parameters
    node_tree.autoExecution.enabled = False

    # Loop input node
    node_tree.nodes.new(type="an_LoopInputNode")
    node_name = demo_id + "loop_in" + node_tree_id
    node_tree.nodes["Loop Input"].name = node_name
    loop_in = node_tree.nodes[node_name]
    loop_in.location = (0, 0)
    loop_in.subprogramName = demo_id + "negative"
    loop_in.newIterator("Float List", "Float")

    # Loop output node (generator)
    node_tree.nodes.new(type = "an_LoopGeneratorOutputNode")
    node_name = demo_id + "loop_out" + node_tree_id
    node_tree.nodes["Loop Generator Output"].name = node_name
    loop_out = node_tree.nodes[node_name]
    loop_out.location = (600, 0)
    loop_out.listDataType = "Float List"

    # Compare node
    node_tree.nodes.new(type="an_CompareNode")
    node_name = demo_id + "compare" + node_tree_id
    node_tree.nodes["Compare"].name = node_name
    compare = node_tree.nodes[node_name]
    compare.location = (225, 0)
    compare.compareType = 'A>B'
    compare.inputs[1].value = 0.00

    # Switch node
    node_tree.nodes.new(type="an_SwitchNode")
    node_name = demo_id + "switch" + node_tree_id
    node_tree.nodes["Switch"].name = node_name
    switch = node_tree.nodes[node_name]
    switch.location = (420, 0)
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

    # auto-execution parameters
    node_tree.autoExecution.enabled = False

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location = (-350, 0)
    grp_in.subprogramName = demo_id + "mesh_data"
    grp_in.newGroupInput("Float List", "Float List")
    grp_in.newGroupInput("Float List", "Float List")

    # Group output node
    node_tree.nodes.new(type="an_GroupOutputNode")
    node_name = demo_id + "grp_out" + node_tree_id
    node_tree.nodes["Group Output"].name = node_name
    grp_out = node_tree.nodes[node_name]
    grp_out.location = (650, 0)
    grp_out.newGroupOutput("Float List", "Results")

    # Invoke multiply_all
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_multiply_all" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_mult_all = node_tree.nodes[node_name]
    inv_mult_all.location = (160, 200)
        # set subprogram
    inv_mult_all_inp = bpy.data.node_groups[demo_id+"multiply_all"].nodes[demo_id + "loop_in" + "_ma"]
    inv_mult_all.subprogramIdentifier = inv_mult_all_inp.identifier

    # Invoke negative
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_negative" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_neg = node_tree.nodes[node_name]
    inv_neg.location = (-40, 0)
        # set subprogram
    inv_neg_inp = bpy.data.node_groups[demo_id+"negative"].nodes[demo_id + "loop_in" + "_neg"]
    inv_neg.subprogramIdentifier = inv_neg_inp.identifier

    # Invoke max_values
    node_tree.nodes.new(type="an_InvokeSubprogramNode")
    node_name = demo_id + "invoke_max_values" + node_tree_id
    node_tree.nodes["Invoke Subprogram"].name = node_name
    inv_mv = node_tree.nodes[node_name]
    inv_mv.location = (-40, -160)
        # set subprogram
    inv_mv_inp = bpy.data.node_groups[demo_id+"max_values"].nodes[demo_id + "grp_in" + "_mv"]
    inv_mv.subprogramIdentifier = inv_mv_inp.identifier

    # Multiply node
    node_tree.nodes.new(type="an_FloatMathNode")
    node_name = demo_id + "math_multiply" + node_tree_id
    node_tree.nodes["Float Math"].name = node_name
    math_mult = node_tree.nodes[node_name]
    math_mult.location = (460, 0)
    math_mult.operation = 'MULTIPLY'

    # forces to update socket inputs/outputs (tada !)
    # TODO: find a better solution
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

def generateCircuit(context, demo_id, circuit_id):
    context.new_node_tree(type="an_AnimationNodeTree", name=demo_id+"circuit_"+circuit_id)
    node_tree = bpy.data.node_groups[demo_id+"circuit_"+circuit_id]
    node_tree_id = "_c"+circuit_id

    # auto-execution parameters
    node_tree.autoExecution.enabled = False

    # Group input node
    node_tree.nodes.new(type="an_GroupInputNode")
    node_name = demo_id + "grp_in" + node_tree_id
    node_tree.nodes["Group Input"].name = node_name
    grp_in = node_tree.nodes[node_name]
    grp_in.location = (-400, 0)
    grp_in.subprogramName = demo_id + "circuit_" + circuit_id

    # Heightmap to quantum circuit node
    node_tree.nodes.new(type="an_HeightmapToQuantumCircuitNode")
    node_name = demo_id + "hmap_to_qu_cir" + node_tree_id
    node_tree.nodes["Heightmap To Quantum Circuit"].name = node_name
    heightmap_to_circuit = node_tree.nodes[node_name]
    heightmap_to_circuit.location = (-180, 0)

    # Quantum circuit to heightmap node
    node_tree.nodes.new(type="an_QuantumCircuitToHeightmapNode")
    node_name = demo_id + "qu_cir_to_hmap" + node_tree_id
    node_tree.nodes["Quantum Circuit To Heightmap"].name = node_name
    circuit_to_heightmap = node_tree.nodes[node_name]
    circuit_to_heightmap.location = (800, 0)

    # Group output node
    node_tree.nodes.new(type="an_GroupOutputNode")
    node_name = demo_id + "grp_out" + node_tree_id
    node_tree.nodes["Group Output"].name = node_name
    grp_out = node_tree.nodes[node_name]
    grp_out.location = (1000, 0)
    grp_out.newGroupOutput("Float List", "Results")

    # Linking everything
    node_tree.links.new(grp_in.outputs[0], heightmap_to_circuit.inputs[0])
    node_tree.links.new(heightmap_to_circuit.outputs[0], circuit_to_heightmap.inputs[0])
    node_tree.links.new(circuit_to_heightmap.outputs[0], grp_out.inputs[0])

def generateMainNodeTree(context, main_tree_id, obj):
    bpy.ops.node.new_node_tree(type="an_AnimationNodeTree", name=main_tree_id+"an_q")
    node_tree = bpy.data.node_groups[main_tree_id+"an_q"]
    node_tree_id = "_main"

    # auto-execution parameters
    node_tree.autoExecution.enabled = False
    node_tree.autoExecution.SceneUpdate = False
    node_tree.autoExecution.treeChanged = True
    node_tree.autoExecution.frameChanged = True
    node_tree.autoExecution.propertyChanged = True

    # Mesh Object Input node
    node_tree.nodes.new(type="an_MeshObjectInputNode")
    node_name = main_tree_id + "mesh_obj_input" + node_tree_id
    node_tree.nodes["Mesh Object Input"].name = node_name
    mesh_obj_inp = node_tree.nodes[node_name]
    mesh_obj_inp.location = (-950, 0)
    mesh_obj_inp.inputs[0].object = obj

    # Separate Vector node
    node_tree.nodes.new(type="an_SeparateVectorNode")
    node_name = main_tree_id + "sep_vecs" + node_tree_id
    node_tree.nodes["Separate Vector"].name = node_name
    sep_vecs = node_tree.nodes[node_name]
    sep_vecs.location = (-750, 0)
    
    inv_circuits = {"x" : None, "y" : None, "z" : None}
    for offset, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        # Invoke mesh_data_c(x/y/z)
        node_tree.nodes.new(type="an_InvokeSubprogramNode")
        node_name = main_tree_id + "invoke_circuit_" + circ_name + node_tree_id
        node_tree.nodes["Invoke Subprogram"].name = node_name
        inv_circuits[circ_name] = node_tree.nodes[node_name]
        inv_circuits[circ_name].location = (-200, 500 + offset*(-350))
            # set subprogram
        subprog_inp = bpy.data.node_groups["an_q_demo_"+"circuit_"+circ_name].nodes["an_q_demo_" + "grp_in" + "_c"+circ_name]
        inv_circuits[circ_name].subprogramIdentifier = subprog_inp.identifier
    
    inv_mesh_data_circuits = {"x" : None, "y" : None, "z" : None}
    for offset, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        # Invoke circuit_(x/y/z)
        node_tree.nodes.new(type="an_InvokeSubprogramNode")
        node_name = main_tree_id + "invoke_mesh_data_" + circ_name + node_tree_id
        node_tree.nodes["Invoke Subprogram"].name = node_name
        inv_mesh_data_circuits[circ_name] = node_tree.nodes[node_name]
        inv_mesh_data_circuits[circ_name].location = (200, 500 + offset*(-500))
            # set subprogram
        subprog_inp = bpy.data.node_groups["an_q_demo_"+"mesh_data"].nodes["an_q_demo_" + "grp_in" + "_md"]
        inv_mesh_data_circuits[circ_name].subprogramIdentifier = subprog_inp.identifier

    # Combine Vector node
    node_tree.nodes.new(type="an_CombineVectorNode")
    node_name = main_tree_id + "comb_vecs" + node_tree_id
    node_tree.nodes["Combine Vector"].name = node_name
    comb_vecs = node_tree.nodes[node_name]
    comb_vecs.location = (600, 0)

    # Mesh Object Output node
    node_tree.nodes.new(type="an_MeshObjectOutputNode")
    node_name = main_tree_id + "mesh_obj_output" + node_tree_id
    node_tree.nodes["Mesh Object Output"].name = node_name
    mesh_obj_out = node_tree.nodes[node_name]
    mesh_obj_out.location = (1080, 0)
    mesh_obj_out.meshDataType = "VERTICES"

    # Object instancer node
    node_tree.nodes.new(type="an_ObjectInstancerNode")
    node_name = main_tree_id + "obj_instancer" + node_tree_id
    node_tree.nodes["Object Instancer"].name = node_name
    mesh_inst = node_tree.nodes[node_name]
    mesh_inst.location = (650, 245)
    mesh_inst.inputs[0].value = 1
    mesh_inst.inputs[1].object = obj
    mesh_inst.copyObjectProperties = True
    mesh_inst.deepCopy = True

    # Object matrix input node
    node_tree.nodes.new(type="an_ObjectMatrixInputNode")
    node_name = main_tree_id + "obj_mat_inp" + node_tree_id
    node_tree.nodes["Object Matrix Input"].name = node_name
    obj_mat_inp = node_tree.nodes[node_name]
    obj_mat_inp.location = (1320, -150)

    # Invert matrix node
    node_tree.nodes.new(type="an_InvertMatrixNode")
    node_name = main_tree_id + "invert_matrix" + node_tree_id
    node_tree.nodes["Invert Matrix"].name = node_name
    invert_mat = node_tree.nodes[node_name]
    invert_mat.location = (1500, -150)

    # Transform object node
    node_tree.nodes.new(type="an_TransformObjectNode")
    node_name = main_tree_id + "transf_obj" + node_tree_id
    node_tree.nodes["Transform Object"].name = node_name
    transf_obj = node_tree.nodes[node_name]
    transf_obj.location = (1700, 0)

    # Object transform output node
    node_tree.nodes.new(type="an_ObjectTransformsOutputNode")
    node_name = main_tree_id + "obj_transf_out" + node_tree_id
    node_tree.nodes["Object Transforms Output"].name = node_name
    obj_transf_out = node_tree.nodes[node_name]
    obj_transf_out.location = (1900, 0)
    obj_transf_out.useLocation = True, True, True

    # Data interface node
    node_tree.nodes.new(type="an_DataInterfaceNode")
    node_name = main_tree_id + "data_interface" + node_tree_id
    node_tree.nodes["Data Interface"].name = node_name
    data_interface = node_tree.nodes[node_name]
    data_interface.location = (2100, 0)
    data_interface.dataDirection = "EXPORT"

    # forces to update socket inputs/outputs (tada !)
    # TODO: find a better solution
    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
    # Linking everything
        # Invoke mesh_data_c(x/y/z) output to combine vector inputs
    for index, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        node_tree.links.new(inv_mesh_data_circuits[circ_name].outputs[0], comb_vecs.inputs[index])
        # Invoke circuit_(x/y/z) output to invoke mesh_data_c(x/y/z)
    for circ_name in ["x", "y", "z"]:
        node_tree.links.new(inv_circuits[circ_name].outputs[0], inv_mesh_data_circuits[circ_name].inputs[0])
        # Separate vector outputs to invoke circuit_(x/y/z)
    for index, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        node_tree.links.new(sep_vecs.outputs[index], inv_circuits[circ_name].inputs[0])
        # Mesh object output out to Seperate vector inp
    node_tree.links.new(mesh_obj_inp.outputs[1], sep_vecs.inputs[0])
        # Separate vector outputs to invoke mesh_data_c(x/y/z)
    for index, circ_name in [(0, "x"), (1, "y"), (2, "z")]:
        node_tree.links.new(sep_vecs.outputs[index], inv_mesh_data_circuits[circ_name].inputs[1])
        # Combine vector output to Mesh object output input
    node_tree.links.new(comb_vecs.outputs[0], mesh_obj_out.inputs[1])
        # Enables input mesh object output
    mesh_obj_out.inputs[1].isUsed = True
        # Object instancer output to Mesh object output input
    node_tree.links.new(mesh_inst.outputs[0], mesh_obj_out.inputs[0])
        # Mesh object output to Object matrix input
    node_tree.links.new(mesh_obj_out.outputs[0], obj_mat_inp.inputs[0])
        # Object matrix input out to Invert Matrix input
    node_tree.links.new(obj_mat_inp.outputs[0], invert_mat.inputs[0])
        # Invert Matrix output to Transform Object input
    node_tree.links.new(invert_mat.outputs[0], transf_obj.inputs[1])
        # Mesh object output to Transform Object input
    node_tree.links.new(mesh_obj_out.outputs[0], transf_obj.inputs[0])
        # Transform Object output to Object transforms output in
    node_tree.links.new(transf_obj.outputs[0], obj_transf_out.inputs[0])
        # Data Interface input to Transform Object output out
    node_tree.links.new(obj_transf_out.outputs[0], data_interface.inputs[0])

        # Set offset of the copied object :
    obj_transf_out.inputs[1].value[1] = 5.0
    # TODO: find a better solution for this offset (maybe in function of the target object)

    # forces to update socket inputs/outputs (tada !)
    # TODO: find a better solution
    bpy.context.scene.frame_set(bpy.data.scenes['Scene'].frame_current)
