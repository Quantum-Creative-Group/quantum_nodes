from qiskit import execute
from animation_nodes.base_types import AnimationNode
from bpy.types import Node


class QuantumGateZNode(Node, AnimationNode):
    bl_idname = "an_QuantumGateZNode"
    bl_label = "Quantum Gate Z"
    bl_width_default = 160
    errorHandlingType = "EXCEPTION"

    def setup(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input_circuit")
        self.newInputSocket()
        self.newOutput("Quantum Circuit", "Output Circuit", "output_circuit")

    def draw(self, layout):
        row = layout.row(align=True)
        self.invokeFunction(row, "newInputSocket",
                            text="Add Other Gate",
                            description="Create a new input socket",
                            icon="PLUS")
        self.invokeFunction(row, "removeUnlinkedInputs",
                            description="Remove unlinked inputs",
                            confirm=True,
                            icon="X")

    def getInputSocketVariables(self):
        socketMapping = {}
        socketMapping["input_circuit"] = "inputCircuit"
        for i, socket in enumerate(self.inputs[:]):
            if socket.name != "Input Circuit":
                socketMapping[socket.identifier] = "element_" + str(i)
        return socketMapping

    def getExecutionCode(self, required):
        for i in range(len(self.inputs) - 1):
            yield f"if element_{i} >= inputCircuit.num_qubits:"
            yield "    output_circuit = inputCircuit"
            yield "    self.raiseErrorMessage(\"The qubit index must be lower than \" + str(inputCircuit.num_qubits))"
            yield f"if element_{i} < 0:"
            yield "    output_circuit = inputCircuit"
            yield "    self.raiseErrorMessage(\"The qubit index must be positive.\")"
            yield "else:"
            yield f"    inputCircuit.z(element_{i})"
        yield "output_circuit = inputCircuit"

    def newInputSocket(self):
        socket = self.newInput("Integer", "Qubit Index", minValue=0)
        socket.dataIsModified = True
        socket.display.text = True
        socket.text = "Qubit Index"
        socket.removable = True
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
