import bpy
from qiskit import *
from bpy.props import *
from animation_nodes.base_types import AnimationNode

modeItems = [
    ("NUMBER", "Number", "Create quantum circuit from number of quibts", "", 0),
    ("QREGISTER", "Quantum Register", "Create quantum circuit from quantum register", "", 1),
    ("QCREGISTER", "Quantum and Classical Registers", "Create quantum circuit from quantum and classical register", "", 2)
]

class InitQuantumCircuitNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_InitQuantumCircuitNode"
    bl_label = "Init Quantum Circuit"

    mode = EnumProperty(name = "Mode", default = "NUMBER",
        items = modeItems, update = AnimationNode.refresh)

    def create(self):
        if self.mode == "NUMBER":
            self.newInput("Integer", "Number Of Qubits", "number_of_qubits")
        if self.mode == "QREGISTER":
            self.newInput("Quantum Register", "Quantum Register", "quantum_register")
        if self.mode == "QCREGISTER":
            self.newInput("Quantum Register", "Quantum Register", "quantum_register")
            self.newInput("Classical Register", "Classical Register", "classical_register")
        self.newOutput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")

    def draw(self, layout):
        layout.prop(self, "mode")

    def getExecutionFunctionName(self):
        if self.mode == "NUMBER":
            return "execute_Number"
        elif self.mode == "QREGISTER":
            return "execute_QRegister"
        elif self.mode == "QCREGISTER":
            return "execute_QCRegister"

    def execute_Number(self, number_of_qubits):
        try:
            return QuantumCircuit(number_of_qubits)
        except:
            return
        
    def execute_QRegister(self, quantum_register):
        try:
            return QuantumCircuit(quantum_register)
        except:
            return

    def execute_QCRegister(self, quantum_register,classical_register):
        try:
            return QuantumCircuit(quantum_register,classical_register)
        except:
            return

