from bpy.types import Node
from bpy.props import EnumProperty

from animation_nodes.base_types import AnimationNode


class QuantumMeasureNode(Node, AnimationNode):
    """Measure selected qubits and get the output."""

    bl_idname = "an_QuantumMeasureNode"
    bl_label = "Quantum Measure"

    mode: EnumProperty(
        name="Mode",  # noqa F821
        default="ONE",  # noqa F821
        items=[
            ("ONE", "Measure on qubit", "Measure one qubit on a specific bit", "", 0),  # noqa F821
            ("ALL", "Measure all qubits", "Measure all qubits", "", 1)  # noqa F821
        ],
        update=AnimationNode.refresh
    )

    def create(self):
        if self.mode == "ONE":
            self.newInput("Quantum Circuit", "Input Quantum Circuit", "input_quantum_circuit")
            self.newInput("Integer", "Qubit Index", "qubit_index", value=0, minValue=0)
            self.newInput("Integer", "Bit Index", "bit_index", value=0, minValue=0)
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

    def execute_One(self, input_quantum_circuit, qubit_index, bit_index):
        try:
            input_quantum_circuit.measure(qubit_index, bit_index)
            return input_quantum_circuit
        except BaseException:
            return

    def execute_All(self, input_quantum_circuit):
        input_quantum_circuit.measure_all()
        return input_quantum_circuit
