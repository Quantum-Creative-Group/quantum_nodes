Input nodes
===========


.. note::
    |   This section of the documentation is a list of all the nodes that have been implemented in Quantum Nodes. 
    |   We recommend you try and practice all these nodes in Blender to really see what they can create as the content of this list can be difficult to visualize.


* :ref:`classical-register`
* :ref:`quantum-register`
* :ref:`quantum-circuit`


.. _classical-register:

Init Classical Register
#######################

|   **Input:** Integer (number of qubits to put in the classical register)
|   **Output:** Classical Register
|
|   **Usage:** Calls the ``ClassicalRegister()`` Qiskit function to create a classical register of the length of the integer given as a parameter.
|   

.. image:: /images/nodes/init_classical_register.png
    :width: 60%
    :alt: Classical register 
    :align: center
    :class: img-rounded
    
|


.. _quantum-register:

Init Quantum Register
#####################

|   **Input:** Integer (number of qubits to put in the quantum register)
|   **Output:** Quantum Register
|
|   **Usage:** Calls the ``QuantumRegister()`` Qiskit function to create a quantum register of the length of the integer given as a parameter.
|   

.. image:: /images/nodes/init_quantum_register.png
    :width: 60%
    :alt: Quantum register 
    :align: center
    :class: img-rounded
    
|


.. _quantum-circuit:
    
Init Quantum Circuit
####################

|   **Input 1:** Integer (number of qubits to put in the quantum circuit)
|   **Input 2:** Quantum register
|   **Input 3:** Quantum register and Classical register
|   **Output:** Quantum Circuit
|
|   **Usage:** Calls the ``QuantumCircuit()`` Qiskit function to create a quantum circuit.
|   If the input is an integer, a circuit will be created with that number of qubits.
|   If the input is a quantum register, the quantum circuit will be initialised from that register.
|   

.. image:: /images/nodes/init_quantum_circuit1.png
    :width: 60%
    :alt: Quantum circuit 
    :align: center
    :class: img-rounded
    
|

.. image:: /images/nodes/init_quantum_circuit2.png
    :width: 60%
    :alt: Quantum circuit 
    :align: center
    :class: img-rounded
    
|

.. image:: /images/nodes/init_quantum_circuit3.png
    :width: 60%
    :alt: Quantum circuit 
    :align: center
    :class: img-rounded
    
|