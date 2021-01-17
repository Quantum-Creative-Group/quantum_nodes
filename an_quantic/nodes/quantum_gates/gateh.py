import bpy
from qiskit import *
from bpy.props import *
from animation_nodes.base_types import AnimationNode

class QuantumGateHNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumGateHNode"
    bl_label = "Quantum GateH"

    def setup(self):
        self.newInput("Quantum Circuit", "Input Circuit", "input_circuit")
        self.newInputSocket()
        self.newOutput("Quantum Circuit", "Output Circuit", "output_circuit") 
        
        #self.newInput("Node Control", "...")

   # def create(self):
   #     print ("create")
   #     self.newInput("Quantum Circuit", "Input Circuit", "input_circuit")
   #     self.newOutput("Quantum Circuit", "Output Circuit", "output_circuit")  

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
            if (socket.name != "Input Circuit") :
                socketMapping[socket.identifier] = "element_"+str(i)
        
            #link = node.inputs[0].links[0] #gets the link from the input
           # print() link.from_socket.name 
        #socketMapping = {socket.identifier : "element_" + str(i) for i, socket in enumerate(self.inputs[1:])}

        
        print (socketMapping)
        return socketMapping

    def getExecutionCode(self, required):
        for i in range(len(self.inputs) - 1) :
            yield "try:"
            yield f"    if (element_{i} < inputCircuit.num_qubits) :"
            yield f"        inputCircuit.h(element_{i})"
            yield "except:"
            yield "    output_circuit = inputCircuit"
            yield "    self.raiseErrorMessage('Failed to do Quantum operation.')"
        yield "output_circuit = inputCircuit"
        

#    def edit(self):  
#        print ("edit")
#        emptySocket = self.inputs["..."]
#        origin = emptySocket.directOrigin
#        if origin is None: return
#        socket = self.newInputSocket()
#        socket.linkWith(origin)
#        emptySocket.removeLinks()


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

