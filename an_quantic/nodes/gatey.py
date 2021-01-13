import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateY(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateY"
    bl_label = "Quantum GateY"

    def create(self):
        self.newInput("QuantumCircuit", "Input", "input")
        self.newOutput("QuantumCircuit", "Output", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.y(j)
            return input
        except:
            return