import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateX(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateX"
    bl_label = "Quantum GateX"

    def create(self):
        self.newInput("QuantumCircuit", "Input", "input")
        self.newOutput("QuantumCircuit", "Output", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.x(j)
            return input
        except:
            return