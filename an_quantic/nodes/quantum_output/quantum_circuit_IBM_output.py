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
    bl_width_default = 210
    errorHandlingType = "EXCEPTION"
    _provider = Provider()

    token: StringProperty(name = "Token",
        description = "Copy your IBM quantum experience token here",
        update = propertyChanged)

    initialized: BoolProperty(name = "Initialized", default = False,
        description = "If the node has been initialized")

    remaining_jobs: IntProperty(name = "Remaining jobs",
        description = "The number of remaining jobs for a backend")

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
            if IBMQ.active_account() == None:   # test if the IBMQ account is already loaded
                try:
                    #IBMQ.enable_account("8d1a1a42b2266ae891741209ae6fc32a696df8fb4193ca47399494d0925a595fb7ff221feb127051d8fba24a2688dde9dc6958ff11ad0f1ecba1d4681172539") #8d1a1a42b2266ae891741209ae6fc32a696df8fb4193ca47399494d0925a595fb7ff221feb127051d8fba24a2688dde9dc6958ff11ad0f1ecba1d46811725395
                    IBMQ.load_account() # needs a connection to internet! (TODO: manage exceptions)
                except Exception as e:  # two possibilities: either not connected to internet or doesn't have an IBM account
                    error_msg = ""
                    for msg in e.args:
                        error_msg += msg + "\n"
                    self.raiseErrorMessage(error_msg)


            # TODO: try if load account fails and in catch ask for token (w/ self.raiseError maybe?)
            self.initialized = True

    def setup(self):
        node_tree = bpy.context.space_data.edit_tree
        node_tree.autoExecution.sceneUpdate = False
        node_tree.autoExecution.treeChanged = False
        node_tree.autoExecution.frameChanged = False
        node_tree.autoExecution.propertyChanged = False

    def create(self):
        self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
        self.newOutput("Generic", "Output State", "output_state")

    def draw(self, layout):
        layout.prop(self, "backendMenu")
        layout.label(text = "Number of jobs remaining: " + str(self.remaining_jobs), icon = "INFO")
        self.invokeFunction(layout, "executeTree", text = "Send")

    def executeTree(self):
        node_tree = bpy.context.space_data.edit_tree
        node_tree.execute()

    def drawAdvanced(self, layout):
        layout.prop(self, "token")
        col = layout.column()

    # def getExecutionFunctionName(self):
    #     return "execute"

    def execute(self, quantum_circuit):
        backend = self._provider.get_provider().get_backend(self.backendMenu)   # TODO: fix --> Exception: node is not refreshable
        self.remaining_jobs = backend.remaining_jobs_count()
        if backend.status().operational == False:
            self.raiseErrorMessage("This system is offline for now")
        if (quantum_circuit.num_qubits > backend.configuration().n_qubits):
            self.raiseErrorMessage("This system doesn't compute enough qubits: " + str(backend.configuration().n_qubits))
        # ---execute() works but is not optimized for more important jobs
        # quantum_circuit.measure_all() # should find a way to get rid of this but it doesn't work without any measure
        # job = execute(quantum_circuit, backend)
        # ---there are 2 ways of computing this (lign ahead or the two above)
        qobj = assemble(transpile(quantum_circuit, backend=backend), backend=backend)
        job = backend.run(qobj)
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