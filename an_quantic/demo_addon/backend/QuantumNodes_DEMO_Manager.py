import bpy, os, sys
import math
import copy

from . CircuitManager import CircuitManager
from . NodeTreeManager import NodeTreeManager

class QuantumNodes_DEMO_Manager():

    def __init__(self):
        self.max_qubits = 10
        self.max_gates = 5
        self.possible_gates = ["h", "x", "y"]
        self.circuits = {"x": None, "y": None, "z": None}
        self.selected_circuit = 'x'
        self.ntm = NodeTreeManager()
        self.nb_qubits = None
        self.nt_initialized = False
        self.target = None

    def getSelectedCircuit(self):
        return self.circuits[self.selected_circuit]

    def initializeDemoNodeTree(self):
        if(not self.nt_initialized):
            self.ntm.generateNodeTree(self.target)
            self.nt_initialized = True

    def setNewTarget(self, new_target):
        # resets circuits
        for circuit_name in list(self.circuits.keys()):
            circuit = self.circuits[circuit_name]
            if(circuit != None):
                circuit.reset()
                self.ntm.resetAllGates()
        # sets new target
        self.setNewCircuits(new_target)
        self.target = new_target
        self.ntm.updateTarget(new_target)

    def setNewCircuits(self, obj):
        self.nb_qubits = int(math.ceil(math.log(len(obj.data.vertices))/math.log(2)))
        for circuit_name in list(self.circuits.keys()): self.circuits[circuit_name] = CircuitManager(self.nb_qubits, self.max_gates)
        self.ntm.last_circuits = copy.deepcopy(self.circuits)
    
    def updateNodeTree(self):
        self.ntm.update(self.circuits)