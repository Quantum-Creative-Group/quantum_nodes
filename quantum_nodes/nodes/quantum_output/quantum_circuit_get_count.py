import bpy
from qiskit import Aer
from qiskit import execute
from animation_nodes.base_types import AnimationNode

class QuantumCircuitGetCountNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitGetCountNode"
    bl_label = "Quantum Circuit Get Count"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Integer", "Number of Shots", "shots", value = 1024, minValue = 1)
        self.newOutput("Quantum Count", "Counts", "counts")

    def execute(self, quantum_circuit, shots):
        if(shots < 1):
            self.raiseErrorMessage("The number of shots must be superior to 1")
        else:
            return execute(quantum_circuit,Aer.get_backend('qasm_simulator')).result().get_counts()