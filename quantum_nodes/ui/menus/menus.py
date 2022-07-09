from bpy.types import Menu

from animation_nodes.ui.node_menu import insertNode


class QN_MT_QuantumGates(Menu):
    """Menu of all quantum gates nodes."""

    bl_idname = "QN_MT_quantum_gates"
    bl_label = "Gates"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_QuantumGateSWAPNode", "Quantum Gate SWAP")
        layout.separator()
        layout.menu("QN_MT_quantum_gates_c", text="C Gates", icon="EVENT_C")
        layout.menu("QN_MT_quantum_gates_r", text="R Gates", icon="EVENT_R")
        # TODO: are these gates necessary now?
        # layout.menu("QN_MT_quantum_gates_to_all", text = "Gates_To_All", icon = "OBJECT_ORIGIN")
        layout.menu("QN_MT_quantum_gates_single_qubit", text="Single_Qubit_Gates", icon="DOT")


class QN_MT_Schrodinger(Menu):
    """Menu of Schrödinger equation simulation nodes."""

    bl_idname = "QN_MT_schrodinger"
    bl_label = "Schrödinger Simulation"

    def draw(self, _context):
        insertNode(self.layout, "an_SchrodingerEquationSimulationNode", "Schrödinger Equation Simulation")


class QN_MT_QuantumBlur(Menu):
    """Menu of Quantum Blur nodes."""

    bl_idname = "QN_MT_quantum_blur"
    bl_label = "Quantum Blur"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_QuantumBlurInputNode", "Quantum Blur Input")
        insertNode(layout, "an_QuantumBlurOutputNode", "Quantum Blur Output")


class QN_MT_Qgan(Menu):
    """Menu of QGAN related nodes."""

    bl_idname = "QN_MT_qgan"
    bl_label = "Quantum GAN"

    def draw(self, _context):
        insertNode(self.layout, "an_qGAN", "qGAN Processing")


class QN_MT_ComplexNumbers(Menu):
    """Menu of complex numbers nodes."""

    bl_idname = "QN_MT_complex_numbers"
    bl_label = "Complex Numbers"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_SplitComplex128", "Split complex128")


class QN_MT_QuantumCircuits(Menu):
    """Menu of circuit related nodes."""

    bl_idname = "QN_MT_init_quantum_circuits"
    bl_label = "Init Quantum Circuit"

    def draw(self, _context):
        layout = self.layout
        insertNode(layout, "an_InitClassicalRegisterNode", "Init Classical Register")
        insertNode(layout, "an_InitQuantumRegisterNode", "Init Quantum Register")
        insertNode(layout, "an_InitQuantumCircuitNode", "Init Quantum Circuit")


class QN_MT_Outputs(Menu):
    """Menu of all output gates nodes."""

    bl_idname = "QN_MT_outputs"
    bl_label = "All Quantum Output"

    def draw(self, _context):
        layout = self.layout
        layout.menu("QN_MT_SUB_visualization", text="Visualization", icon="HIDE_OFF")
        layout.menu("QN_MT_SUB_outputs", text="Quantum Output", icon="ORIENTATION_NORMAL")
