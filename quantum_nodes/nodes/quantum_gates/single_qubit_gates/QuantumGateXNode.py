import bpy
from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node

class QuantumGateXNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateXNode"
    bl_label = "Quantum Gate X"
    bl_width_default = 160
    errorHandlingType = "EXCEPTION"

    def setup(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input_circuit")
        self.newInputSocket()
        self.newOutput("Quantum Circuit", "Output Circuit", "output_circuit") 

    def draw(self, layout):
        row = layout.row(align = True)
        self.invokeFunction(row, "newInputSocket",
            text = "Add Other Gate",
            description = "Create a new input socket",
            icon = "PLUS")
        self.invokeFunction(row, "removeUnlinkedInputs",
            description = "Remove unlinked inputs",
            confirm = True,
            icon = "X")

    def getInputSocketVariables(self):
        socketMapping = {}
        socketMapping["input_circuit"] = "inputCircuit"
        for i, socket in enumerate(self.inputs[:]):
            if socket.name != "Input Circuit":
                socketMapping[socket.identifier] = "element_"+str(i)
        return socketMapping

    def getExecutionCode(self, required):
        for i in range(len(self.inputs) - 1) :
            yield f"if element_{i} < inputCircuit.num_qubits:"
            yield f"    inputCircuit.x(element_{i})"
            yield "else:"
            yield "    output_circuit = inputCircuit"
            yield "    self.raiseErrorMessage(\"Qubit Index can't be larger than the number of qubits in the Input Circuit.\")"
        yield "output_circuit = inputCircuit"

    def newInputSocket(self):
        socket = self.newInput("Integer","Qubit Index", minValue = 0)
        socket.dataIsModified = True
        socket.display.text = True
        socket.text = "Qubit Index"
        socket.removeable = True
        socket.moveable = True
        socket.defaultDrawType = "PREFER_PROPERTY"
        socket.moveUp()
        if len(self.inputs) > 3:
            socket.copyDisplaySettingsFrom(self.inputs[1])
        return socket

    def removeUnlinkedInputs(self):
        for socket in self.inputs[1:-1]:
            if not socket.is_linked:
                socket.remove()