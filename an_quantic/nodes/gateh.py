import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateH(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateH"
    bl_label = "Quantum GateH"

    def create(self):
        self.newInput("QuantumCircuit", "Input", "input")
        self.newOutput("QuantumCircuit", "Output", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.h(j)
            return input
        except:
            return