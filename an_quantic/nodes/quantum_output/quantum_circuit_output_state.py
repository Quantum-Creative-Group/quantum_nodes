import bpy
from qiskit import *
from animation_nodes.base_types import AnimationNode

class QuantumCircuitOutputStateNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitOutputStateNode"
    bl_label = "Quantum Circuit Output State"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newOutput("Vector", "Output State", "output_state")

    def execute(self, quantum_circuit):
        try:
            backend = Aer.get_backend('statevector_simulator')
            job = execute(quantum_circuit, backend)
            result = job.result()
            return result.get_statevector(quantum_circuit,quantum_circuit.num_qubits)
        except:
            return