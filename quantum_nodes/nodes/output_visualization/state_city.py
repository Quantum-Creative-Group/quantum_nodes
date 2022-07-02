import bpy
from bpy.types import Node
from qiskit import (Aer, execute)
from animation_nodes.base_types import AnimationNode
from ... visualization.utils.edit_state_city import editStateCity


class StateCityNode(Node, AnimationNode):
    """Generate a new state city plot."""

    bl_idname = "an_StateCityNode"
    bl_label = "State City"

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newInput("Object", "State City", "state_city")

    def execute(self, quantum_circuit, state_city):
        if state_city is None:
            return
        if (state_city.name != "QuantumCityFaces"):
            return
        try:
            backend = Aer.get_backend('statevector_simulator')
            result = execute(quantum_circuit, backend).result()  # Do the simulation, returning the result
            out_state = result.get_statevector()

            parent = state_city.parent
            for i in range(len(state_city.children)):
                bpy.data.objects.remove(state_city.children[0])
            bpy.data.objects.remove(state_city)
            editStateCity(parent, out_state)
        except BaseException:
            return
