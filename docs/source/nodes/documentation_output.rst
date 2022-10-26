Output nodes
============


.. note::
    |   This section of the documentation is a list of all the nodes that have been implemented in Quantum Nodes. 
    |   We recommend you try and practice all these nodes in Blender to really see what they can create as the content of this list can be difficult to visualize.


* :ref:`circuit-get-count`
* :ref:`quantum-measure`
* :ref:`quantum-circuit-output-state`
* :ref:`quantum-circuit-IBM`


.. _circuit-get-count:

Quantum Circuit Get Count
#########################

|   **Input:** Quantum Circuit
|   **Output:** Counts
|
|   **Usage:** Applies the following code : ``quantum_circuit.measure_all()``
|   ``return execute(quantum_circuit,Aer.get_backend('qasm_simulator')).result().get_counts()``
|   

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/init_quantum_circuit_counts.png
    :width: 60%
    :alt: Quantum circuit get count 
    :align: center
    :class: img-rounded
    
|


.. _quantum-measure:

Init Quantum Register
#####################

|   **Input 1:** Quantum circuit, index of the qubit to measure, index of the qubit from which to measure on
|   **Input 2:** Quantum Circuit 
|
|   **Usage:** Measures the chosen qubit OR all qubits.
|   

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/init_quantum_register.png
    :width: 60%
    :alt: Quantum register 
    :align: center
    :class: img-rounded
    
|


.. _quantum-circuit-output-state:
    
Quantum Circuit Output State
############################

|   **Input 1:** Quantum Circuit
|
|   **Usage:** Returns the state of the circuit.
|   

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/quantum_circuit_output_state.png
    :width: 60%
    :alt: Quantum circuit output state 
    :align: center
    :class: img-rounded
    
|


.. _quantum-circuit-IBM:
    
Quantum Circuit IBM Output
##########################

|   **Input 1:** Quantum Circuit
|
|   **Usage:** Send the quantum circuit to be computed by IBM quantum computers instead of the Blender simulation.
|   

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/ibm.png 
    :width: 60%
    :alt: Quantum circuit ibm output 
    :align: center
    :class: img-rounded
    
|