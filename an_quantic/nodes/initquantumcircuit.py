import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class InitQuantumCircuit(bpy.types.Node, AnimationNode):
    bl_idname = "an_InitQuantumCircuit"
    bl_label = "Init Quantum Circuit"

    def create(self):
        self.newInput("Integer", "Input", "input")
        self.newOutput("QuantumCircuit", "Output", "output")

    def execute(self, input):
        try:
            for j in range(input.num_qubits):
                input.x(j)
            output = input
        except:
            return