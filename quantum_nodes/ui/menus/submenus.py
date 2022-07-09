from bpy.types import Menu

from animation_nodes.ui.node_menu import insertNode


class QN_MT_SUB_Outputs(Menu):
    """Menu of output nodes."""

    bl_idname = "QN_MT_SUB_outputs"
    bl_label = "Quantum Output"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_QuantumCircuitGetCountNode", "Quantum Circuit Get Count")
        insertNode(layout, "an_QuantumCircuitOutputStateNode", "Quantum Circuit Output State")
        insertNode(layout, "an_QuantumMeasureNode", "Quantum Measure")
        insertNode(layout, "an_QuantumCircuitIBMOutputStateNode", "Quantum Circuit IBM Output")


class QN_MT_SUB_QuantumGates(Menu):
    """Menu of C gates nodes."""

    bl_idname = "QN_MT_quantum_gates_c"
    bl_label = "C Gates"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateCHNode", "Quantum Gate CH")
        insertNode(layout, "an_QuantumGateCXNode", "Quantum Gate CX")
        insertNode(layout, "an_QuantumGateCYNode", "Quantum Gate CY")
        insertNode(layout, "an_QuantumGateCZNode", "Quantum Gate CZ")
        insertNode(layout, "an_QuantumGateCCXNode", "Quantum Gate CCX")
        insertNode(layout, "an_QuantumGateCSWAPNode", "Quantum Gate CSWAP")


class QN_MT_SUB_QuantumGatesR(Menu):
    """Menu of R gates nodes."""

    bl_idname = "QN_MT_quantum_gates_r"
    bl_label = "R Gates"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateRXNode", "Quantum Gate RX")
        insertNode(layout, "an_QuantumGateRYNode", "Quantum Gate RY")
        insertNode(layout, "an_QuantumGateRZNode", "Quantum Gate RZ")


class QN_MT_SUB_QuantumGatesSingleQubit(Menu):
    """Menu of single qubits gates nodes."""

    bl_idname = "QN_MT_quantum_gates_single_qubit"
    bl_label = "Single Qubit Gates"

    def draw(self, _context):
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


class QN_MT_SUB_QuantumGatesToAll(Menu):
    """Menu of gates 'to all circuit' nodes."""

    bl_idname = "QN_MT_quantum_gates_to_all"
    bl_label = "Gates To All"

    def draw(self, _context):
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


class QN_MT_SUB_Visualization(Menu):
    """Menu of data visualization nodes."""

    bl_idname = "QN_MT_SUB_visualization"
    bl_label = "Visualization tools"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_BlochSphereNode", "Bloch sphere")
        insertNode(layout, "an_HistogramNode", "Histogram")
        insertNode(layout, "an_StateCityNode", "State city")
        # insertNode(layout, "an_QganHistogramNode", "qGAN Histogram")
