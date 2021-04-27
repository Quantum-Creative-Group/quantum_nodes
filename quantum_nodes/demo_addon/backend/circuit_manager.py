import bpy

class CircuitManager():

    def __init__(self, nb_qubits, mg):
        self.max_gates = mg
        self.data = [[] for i in range(nb_qubits)]

    def pushGate(self, q_index, gate):
       if len(self.data[q_index]) < self.max_gates:
            self.data[q_index].append(gate)

    def popGate(self, q_index):
        if len(self.data[q_index]) > 0:
            self.data[q_index].pop()

    def reset(self):
        self.data.clear()
    
    def __str__(self):
        return str(self.data)