import bpy, os, sys
import math

from . CircuitManager import CircuitManager
from . NodeTreeManager import NodeTreeManager

class QuantumNodes_DEMO_Manager():

    def __init__(self, nb = 3):
        self.possible_gates = ["h", "x", "y"]
        self.circuits = {"x": None, "y": None, "z": None}
        self.selected_circuit = 'x'
        self.ntm = NodeTreeManager()
        self.nb_qubits = None
        self.initialized = False
        self.selected_obj = None

    def get_selected_circuit(self):
        return self.circuits[self.selected_circuit]

    def initializeDemo(self):
        if(not self.initialized):
            self.ntm.generateNodeTree()
            self.initialized = True

    def reset(self):
        for circuit_name in list(self.circuits.keys()): self.circuits[circuit_name].data.clear()

    def createNewCircuit(self, obj):
        self.selected_obj = obj
        self.nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))
        for circuit_name in list(self.circuits.keys()): self.circuits[circuit_name] = CircuitManager(self.nb_qubits)