import bpy
from qiskit import *
from bpy.props import *
from animation_nodes.base_types import AnimationNode

modeItems = [
    ("ONE", "Measure on qubit", "Measure one qubit on a specific bit", "", 0),
    ("ALL", "Measure all qubits", "Measure all qubits", "", 1)
]

class QuantumMeasureNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumMeasureNode"
    bl_label = "Quantum Measure"

    mode = EnumProperty(name = "Mode", default = "ONE",
        items = modeItems, update = AnimationNode.refresh)

    def create(self):
        if self.mode == "ONE":
            self.newInput("Quantum Circuit", "Input Quantum Circuit", "input_quantum_circuit")
            self.newInput("Integer", "Qubit Index", "qubit_index", value = 0, minValue = 0)
            self.newInput("Integer", "Bit Index", "bit_index", value = 0, minValue = 0)
        if self.mode == "ALL":
            self.newInput("Quantum Circuit", "Input Quantum Circuit", "input_quantum_circuit")
        self.newOutput("Quantum Circuit", "Output Quantum Circuit", "output_quantum_circuit")


    def draw(self, layout):
        layout.prop(self, "mode")

    def getExecutionFunctionName(self):
        if self.mode == "ONE":
            return "execute_One"
        if self.mode == "ALL":
            return "execute_All"

    def execute_One(self,input_quantum_circuit, qubit_index ,bit_index):
        try:
            input_quantum_circuit.measure(qubit_index,bit_index)
            return input_quantum_circuit
        except:
            return

    def execute_All(self,input_quantum_circuit):
        try:
            input_quantum_circuit.measure_all()
            return input_quantum_circuit
        except:
            return
    