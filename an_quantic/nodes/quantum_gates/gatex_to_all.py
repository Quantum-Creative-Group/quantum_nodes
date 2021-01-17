import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateXToAllNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateXToAllNode"
    bl_label = "Quantum GateX To All Circuit"
    errorHandlingType = "EXCEPTION"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0,  minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, qubit_index):
        if qubit_index > input.num_qubits:
            self.raiseErrorMessage("Qubit Index can't be larger than the number of qubits in the Input Circuit.")
            return     
        try:
            for j in range(input.num_qubits):
                input.x(j)
            return input
        except:
            self.raiseErrorMessage("Failed to do quantum magic.")
            return