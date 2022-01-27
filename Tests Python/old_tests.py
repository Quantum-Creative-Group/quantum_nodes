import bpy
from animation_nodes.base_types import AnimationNode

import numpy as np

seed = 71
np.random.seed = seed

import matplotlib.pyplot as plt

%matplotlib inline

from qiskit import QuantumRegister, QuantumCircuit, BasicAer
# from qiskit.circuit.library import TwoLocal, UniformDistribution #deprecated
from qiskit.circuit.library import TwoLocal

from qiskit_finance.circuit.library import UniformDistribution

from qiskit.utils import QuantumInstance, algorithm_globals
from qiskit_machine_learning.algorithms import NumPyDiscriminator, QGAN

algorithm_globals.random_seed = seed

modeItems = [
    ("QNUMBER", "Number of Qubits", "Create quantum circuit from number of quibts", "", 0) #,
    #("QCNUMBER", "Number of Qubits and Bits", "Create quantum circuit from number of quibts and number of bits", "", 1)
]


bl_idname = "an_qGAN"
bl_label = "qGAN Processing"


    # ------------- LOAD THE TRAINING DATA --------------

# Number training data samples
N = 1000

# Load data samples from log-normal distribution with mean=1 and standard deviation=1
mu = 1
sigma = 1
real_data = np.random.lognormal(mean=mu, sigma=sigma, size=N)