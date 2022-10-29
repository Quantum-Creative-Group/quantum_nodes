from bpy.types import Node

from qiskit import Aer, execute
from animation_nodes.base_types import AnimationNode


class QuantumCircuitGetCountNode(Node, AnimationNode):
    """Execute the circuit on the qasm simulator and return counts of the result."""

    bl_idname = "an_QuantumCircuitGetCountNode"
    bl_label = "Quantum Circuit Get Count"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Integer", "Number of Shots", "shots", value=1024, minValue=1)
        self.newOutput("Quantum Count", "Counts", "counts")

    def execute(self, quantum_circuit, shots):
        # attention il manque la possibilité de faire le nombre de shots qu'on veut.
        if shots < 1:
            self.raiseErrorMessage("The number of shots must be superior to 1")
        if quantum_circuit.num_clbits < 1:
            self.raiseErrorMessage("There has to be at least one classical bit in the circuit to get the count")
        else:
            return execute(quantum_circuit, Aer.get_backend('qasm_simulator')).result().get_counts()
