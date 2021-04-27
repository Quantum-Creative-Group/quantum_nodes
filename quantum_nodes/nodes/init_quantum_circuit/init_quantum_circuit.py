import bpy
from qiskit import QuantumCircuit
from bpy.props import EnumProperty
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

modeItems = [
    ("QNUMBER", "Number of Qubits", "Create quantum circuit from number of quibts", "", 0),
    ("QCNUMBER", "Number of Qubits and Bits", "Create quantum circuit from number of quibts and number of bits", "", 1),
    ("QREGISTER", "Quantum Register", "Create quantum circuit from quantum register", "", 2),
    ("QCREGISTER", "Quantum and Classical Registers", "Create quantum circuit from quantum and classical register", "", 3)
]

class InitQuantumCircuitNode(Node, AnimationNode):
    bl_idname = "an_InitQuantumCircuitNode"
    bl_label = "Init Quantum Circuit"
    errorHandlingType = "EXCEPTION"

    mode: EnumProperty(name = "Mode", default = "QNUMBER",
        items = modeItems, update = AnimationNode.refresh)

    def create(self):
        if self.mode == "QNUMBER":
            self.newInput("Integer", "Number Of Qubits", "number_of_qubits", value = 1, minValue = 1)
        if self.mode == "QCNUMBER":
            self.newInput("Integer", "Number Of Qubits", "number_of_qubits", value = 1, minValue = 1)
            self.newInput("Integer", "Number Of Bits", "number_of_bits", value = 1, minValue = 1)
        if self.mode == "QREGISTER":
            self.newInput("Quantum Register", "Quantum Register", "quantum_register")
        if self.mode == "QCREGISTER":
            self.newInput("Quantum Register", "Quantum Register", "quantum_register")
            self.newInput("Classical Register", "Classical Register", "classical_register")
        self.newOutput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")

    def draw(self, layout):
        layout.prop(self, "mode")

    def getExecutionFunctionName(self):
        if self.mode == "QNUMBER":
            return "execute_QNumber"
        if self.mode == "QCNUMBER":
            return "execute_QCNumber"
        elif self.mode == "QREGISTER":
            return "execute_QRegister"
        elif self.mode == "QCREGISTER":
            return "execute_QCRegister"

    def execute_QNumber(self, number_of_qubits):
        if(number_of_qubits<1):
            self.raiseErrorMessage("The number of qubits must be superior to 1")
        else:
            return QuantumCircuit(number_of_qubits)

    def execute_QCNumber(self, number_of_qubits,number_of_bits):
        if(number_of_qubits<1):
            self.raiseErrorMessage("The number of qubits must be superior to 1")
            return
        if(number_of_bits<1):
            self.raiseErrorMessage("The number of bits must be superior to 1")
            return
        else:
            return QuantumCircuit(number_of_qubits,number_of_bits)
        
    def execute_QRegister(self, quantum_register):
        return QuantumCircuit(quantum_register)

    def execute_QCRegister(self, quantum_register,classical_register):
        return QuantumCircuit(quantum_register,classical_register)