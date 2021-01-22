import bpy
import time
from qiskit import IBMQ
from qiskit import execute
from qiskit.compiler import transpile, assemble
from qiskit.providers.jobstatus import JobStatus, JOB_FINAL_STATES
from animation_nodes.base_types import AnimationNode
from bpy.props import * # ...Property
from animation_nodes.events import propertyChanged
from animation_nodes.events import executionCodeChanged


class Provider():
    def __init__(self):
        self.provider = None

    def get_provider(self):
        if self.provider == None:
            self.provider = IBMQ.providers()[0]
        return self.provider


class QuantumCircuitIBMOutputStateNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_QuantumCircuitIBMOutputStateNode"
    bl_label = "Quantum Circuit IBM Output State"
    bl_width_default = 180
    errorHandlingType = "EXCEPTION"
    _provider = Provider()

    token: StringProperty(name = "Token",
        description = "Copy your IBM quantum experience token here",
        update = propertyChanged)

    initialized: BoolProperty(name = "Initialized", default = False,
        description = "If the node has been initialized")

    def item_callback(self, context):
        return [ (sys.name(), sys.name(), "number of qubits: " + str(sys.configuration().n_qubits)) for sys in self._provider.get_provider().backends() ]
        # backendItems = []
        # for sys in self._provider.get_provider().backends():
        #     # if sys.status().operational == True:  # TODO: fix --> make everything rly slow, idk why
        #         backendItems.append( (sys.name(), sys.name(), "number of qubits: " + str(sys.configuration().n_qubits)) )
        # return backendItems

    backendMenu: EnumProperty(
        items = item_callback,
        name = "Backend",
        description = "Choose a system",
        # default = "ibmq_qasm_simulator",  # can't set a default value...?
        update = AnimationNode.refresh,
        get = None,
        set = None)

    def __init__(self):
        if not self.initialized:
            if IBMQ.active_account() == None:
                IBMQ.load_account() # needs a connection to internet! (TODO: manage exceptions)
            # TODO: try if load account fails and in catch ask for token (w/ self.raiseError maybe?)
            self.initialized = True

    def setup(self):
        # print("setup")
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newOutput("Generic", "Output State", "output_state")
    
    def draw(self, layout):
        # print("draw")
        layout.prop(self, "backendMenu")

    def drawAdvanced(self, layout):
        layout.prop(self, "token")
        col = layout.column()

    def getExecutionFunctionName(self): # doesn't call the execute function if I don't do it that way
        return "execute"

    def execute(self, quantum_circuit):
        backend = self._provider.get_provider().get_backend(self.backendMenu)   # TODO: fix --> Exception: node is not refreshable
        if (quantum_circuit.num_qubits > backend.configuration().n_qubits):
            self.raiseErrorMessage("This system doesn't compute enough qubits: " + str(backend.configuration().n_qubits))
        # ---execute() works but is not optimized for more important jobs
        job = execute(quantum_circuit, backend)
        # the other method should be better but doesn't return get_counts
        # qobj = assemble(transpile(quantum_circuit, backend=backend), backend=backend)
        # qobj = compile(quantum_circuit, backend, shots=2000)
        # job = backend.run(qobj)

        start_time = time.time()
        job_status = job.status()
        while job_status not in JOB_FINAL_STATES:
            print(f'Status @ {time.time()-start_time:0.0f} s: {job_status.name},'
                f' est. queue position: {job.queue_position()}')
            # time.sleep(10)
            job_status = job.status()

        # ---idk what's the difference
        # retrieved_job = backend.retrieve_job(job.job_id())
        # result = retrieved_job.result()
        result = job.result()
        # ---feel like we need a measure to get a proper result (???)
        return result.get_counts()