from bpy.types import Node
from qiskit import (Aer, execute)
from animation_nodes.base_types import AnimationNode

class QuantumCircuitOutputStateNode(Node, AnimationNode):
    bl_idname = "an_QuantumCircuitOutputStateNode"
    bl_label = "Quantum Circuit Output State"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newOutput("Vector", "Output State", "output_state")

    def execute(self, quantum_circuit):
        backend = Aer.get_backend('statevector_simulator') # Tell Qiskit how to simulate our circuit
        result = execute(quantum_circuit,backend).result() # Do the simulation, returning the result
        out_state = result.get_statevector()
        return out_state