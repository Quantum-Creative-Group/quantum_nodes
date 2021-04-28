import copy
from math import (ceil, log)

from . circuit_manager import CircuitManager
from . node_tree_manager import NodeTreeManager

class QuantumNodesDEMOManager():
    # TODO: find a way to save these data

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
        """
        Returns the circuit corresponding the selected axis in the UI
        It returns a CircuitManager, not a list
        """
        return self.circuits[self.selected_circuit]

    def initializeDemoNodeTree(self):
        """
        Builds the demo node tree and links the target to the tree
        """
        if not self.nt_initialized:
            self.ntm.generateNodeTree(self.target)
            self.nt_initialized = True

    def setNewTarget(self, new_target):
        """
        Sets the new target and resets everything (circuits in the UI + node trees)
        """
        # Resets circuits
        self.resetCircuits()
        # Sets new target
        self.setNewCircuits(new_target)
        self.target = new_target
        target_updated = self.ntm.updateTarget(new_target)
        if not target_updated:
            # the target has not been updated because the node trees
            # do not exist anymore, so, reset eveything
            self.target = None
            self.nt_initialized = False

    def setNewCircuits(self, obj):
        """
        Sets the new circuit
        The size depends on the number of vertices of the target
        """
        self.nb_qubits = int(ceil(log(len(obj.data.vertices)) / log(2)))
        for circuit_name in list(self.circuits.keys()): self.circuits[circuit_name] = CircuitManager(self.nb_qubits, self.max_gates)
        self.ntm.last_circuits = copy.deepcopy(self.circuits)
    
    def updateNodeTree(self):
        """
        Updates the node tree so that it correponds to the represented circuits in the UI
        """
        self.ntm.update(self.circuits)

    def resetCircuits(self):
        """
        Resets the circuits and the corresponding node trees
        """
        for circuit_name in list(self.circuits.keys()):
            circuit = self.circuits[circuit_name]
            if circuit != None:
                circuit.reset()
                self.ntm.resetAllGates()
    
    def removeAll(self):
        self.resetCircuits()
        self.ntm.removeAllTrees()
        self.nt_initialized = False
        self.target = None
        return