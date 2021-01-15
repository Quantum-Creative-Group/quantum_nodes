import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateHNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateHNode"
    bl_label = "Quantum GateH"

    def create(self):
        self.newInput("Integer", "Qubit Index", "qubit_index")
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.h(j)
            return input
        except:
            return