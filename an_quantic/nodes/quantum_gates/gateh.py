import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumGateHNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateHNode"
    bl_label = "Quantum GateH"

    def create(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input")
        self.newInput("Integer", "Qubit Index", "qubit_index", value = 0,  minValue = 0)
        self.newOutput("Quantum Circuit", "Output Circuit", "output")

    def execute(self, input, qubit_index):
        try:
         #   if (input.number_of_qubits >= qubit_index):
                input.h(qubit_index)
                return input
        #    else :
        #        return
        except:
            return