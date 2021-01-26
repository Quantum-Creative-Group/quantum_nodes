# import bpy
# from qiskit import *
# from qiskit import IBMQ
# # from IBMQ.exceptions import *
# from animation_nodes.base_types import AnimationNode

# class QuantumCircuitOutputStateNode(bpy.types.Node, AnimationNode):
#     bl_idname = "an_QuantumCircuitIBMOutputStateNode"
#     bl_label = "Quantum Circuit IBM Output State"
#     provider = IBMQ.load_account()  # find a way to initialize once (in a config file maybe?)


#     def log(self):
#         # the default provider the user has access to
#         # print("into log")
#         # IBMQ.save_account('f4f77e30225d4500855d9d6c37643e6e56ee0e96e0feff4109817073148e0962b99eacc7adf2d0dda85bc84d158c2737074319a88189287abf7634a519f8318a')
#         # IBMQ.load_account() # Load account from disk
#         # provider = IBMQ.enable_account(f4f77e30225d4500855d9d6c37643e6e56ee0e96e0feff4109817073148e0962b99eacc7adf2d0dda85bc84d158c2737074319a88189287abf7634a519f8318a)
#         # print("provider OK")
#         return provider
#         # to have a different provider, see IBMQ.get_provider()

#     def compute(self, quantum_circuit):
#         # provider = IBMQ.load_account()
#         # print("account logged")
#         # backend = provider.backends.ibmq_vigo
#         # print("ah")
#         simulator_backend = provider.backends.ibmq_qasm_simulator
#         print(provider)
#         qobj = assemble(transpile(quantum_circuit, backend=backend), backend=backend)
#         # print("qobj")
#         job = backend.run(qobj)
#         # print("job")
#         # retrieve_job = backend.retrieve_job(job.job_id())
#         retrieve_job = job.result()
#         return retrieve_job.get_statevector(quantum_circuit, quantum_circuit.num_qubits)

#     def create(self):
#         self.newInput("Quantum Circuit", "Quantum Circuit", "quantum_circuit")
#         # self.newInput("Text", "IBM Quantum Experience Token", "token")
#         self.newOutput("Vector", "Output State", "output_state")

#     def execute(self, quantum_circuit):
#                 # TODO: display the max number of jobs and how many are currently running --> backend.job_limit() / remaining_jobs_count()
#                 # give the opportunity to choose the backend? --> provider.get_backend('ibmq_qasm_simulator') + least_busy(backends[, reservation_lookahead])
#                 # show when it is running --> status = backend.status()
#                 # --see except

#         try:
#             # provider = self.log()
#             # backends = provider.backends()  # returns all the backends available to this account
#             # simulator_backend = provider.get_backend('ibmq_qasm_simulator')   # could be the default value (?)
#             return self.compute(provider, quantum_circuit)
#         except: # TODO: catch the error raised by IBM and display it --> IBMQAccountCredentialsInvalidToken
#             # self.raiseErrorMessage()
#             # print("oh no")
#             return