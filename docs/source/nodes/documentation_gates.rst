Quantum Gates
=============


.. note::
    |   This section of the documentation is a list of all the nodes that have been implemented in Quantum Nodes. 
    |   We recommend you try and practice all these nodes in Blender to really see what they can create as the content of this list can be difficult to visualize.


#. :ref:`single-qubit-gates`
    * :ref:`gate-all`
    * :ref:`gate-H`
    * :ref:`gate-ID`
    * :ref:`gate-S`
    * :ref:`gate-SDG`
    * :ref:`gate-T`
    * :ref:`gate-TDG`
    * :ref:`gate-X`
    * :ref:`gate-Y`
    * :ref:`gate-Z`

#. :ref:`rotation-gates`
    * :ref:`gate-RX`
    * :ref:`gate-RY`
    * :ref:`gate-RZ`

#. :ref:`controlled-not-gates`
    * :ref:`gate-CX-CY-CZ-CH`

#. :ref:`others`
    * :ref:`gate-CCX`
    * :ref:`gate-SWAP`
    * :ref:`gate-CSWAP`


.. _single-qubit-gates:

Single-qubit gates
******************


.. note::
    The following nodes send errors if the indices go beyond the number of qubits in the circuit but the number of qubit indexes is up to the user.


.. _gate-all:

Gate to all circuit
###################

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the H, ID, D, SDG, T, TSG, X, Y or Z gates to all qubits in the circuit.
|   
|   **Description:** The Hadamard gate is a single-qubit operation that maps the basis state ∣0⟩ to 2​∣0⟩+∣1⟩​ and ∣1⟩ to 2​∣0⟩−∣1⟩​, thus creating an equal superposition of the two basis states.
|   **Expected result:** The Hadamard gate can be expressed as a 90º rotation around the Y-axis, followed by a 180º rotation around the X-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_all.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-H:

Gate H
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the H gate to all qubit indices requested by the user.
|   
|   **Description:** The Hadamard gate is a single-qubit operation that maps the basis state ∣0⟩ to 2​∣0⟩+∣1⟩​ and ∣1⟩ to 2​∣0⟩−∣1⟩​, thus creating an equal superposition of the two basis states.
|   **Expected result:** The Hadamard gate can be expressed as a 90º rotation around the Y-axis, followed by a 180º rotation around the X-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-ID:

Gate ID
#######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the ID gate to all qubit indices requested by the user.
|
|   **Expected result:** This gate will not show visible results as it is a "do-nothing" gate.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-S:

Gate S
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the S gate to all qubit indices requested by the user.
|
|   **Description:** The S gate (or Phase gate) is a single-qubit operation.
|   The S gate is equivalent to the RZ gate for the angle pi/2. 
|   **Expected result:** The S gate represents a 90-degree rotation around the z-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-SDG:

Gate SDG
########

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the SDG gate to all qubit indices requested by the user.
|
|   **Description:** The S Dagger Gate (SDG gate) is the conjugate transpose (inverse) of the S gate.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-T:

Gate T
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the T gate to all qubit indices requested by the user.
|
|   **Description:** The T gate is a single-qubit operation.
|   The T gate is equivalent to the RZ gate for the angle pi/4.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-TDG:

Gate TDG
########

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the TDG gate to all qubit indices requested by the user.
|
|   **Description:** The T Dagger Gate (TDG gate) is the conjugate transpose (inverse) of the T gate.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|
 

.. _gate-X:

Gate X
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the X gate to all qubit indices requested by the user.
|
|   **Description:** The X or Pauli-X gate is a single-qubit rotation through π radians around the x-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|
 

.. _gate-Y:

Gate Y
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the Y gate to all qubit indices requested by the user.
|
|   **Description:** The Y or Pauli-Y gate is a single-qubit rotation through π radians around the y-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-Z:

Gate Z
######

|   **Input:** Quantum Circuit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the Z gate to all qubit indices requested by the user.
|
|   **Description:** The Z or Pauli-Z gate is a single-qubit rotation through π radians around the z-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_sdg_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _rotation-gates:

Rotation gates
**************


.. _gate-RX:

Gate RX
#######

|   **Input:** Quantum circuit, index of the target qubit to which we want to apply the gate, angle of rotation
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the RX gate to a chosen qubit depending on the angle provided.
|
|   **Description:** The Rx gate is one of the Rotation operators. The Rx gate is a single-qubit rotation through angle θ (radians) around the x-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_rz_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-RY:

Gate RY
#######

|   **Input:** Quantum circuit, index of the target qubit to which we want to apply the gate, angle of rotation
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the RY gate to a chosen qubit depending on the angle provided.
|
|   **Description:** The Ry gate is one of the Rotation operators. The Ry gate is a single-qubit rotation through angle θ (radians) around the y-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_rz_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-RZ:

Gate RZ
#######

|   **Input:** Quantum circuit, index of the target qubit to which we want to apply the gate, angle of rotation
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the RZ gate to a chosen qubit depending on the angle provided.
|
|   **Description:** The Rz gate is one of the Rotation operators. The Ry gate is a single-qubit rotation through angle θ (radians) around the y-axis.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_rz_and_others.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _controlled-not-gates:

NOT gates
*********


.. _gate-CX-CY-CZ-CH:

Gates CX, CY, CZ, CH
####################

|   **Input:** Quantum circuit, index of the control qubit, index of the target qubit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the CX, CY, CZ or CH gate to a target qubit depending on a control qubit specified by the user.
|
|   **Description:** The CNOT gate is two-qubit operation, where the first qubit is usually referred to as the control qubit and the second qubit as the target qubit. 
|   The CX, CY, CZ, CH gates leave the control qubit unchanged and performs a X, Y, Z or H gate on the target qubit when the control qubit is in state ``∣1⟩`` or leave the target qubit unchanged when the control qubit is in state ∣0⟩.
|   Simply, these gates apply a X, Y, Z or H gate on the target qubit if the control qubit is in the ``|1⟩`` state.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_cy_and_others.png 
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _others:

Other gates
***********


.. _gate-CCX:

Gate CCX
########

|   **Input:** Quantum circuit, index of a first qubit, index of second qubit, index of the target qubit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the X gate to a target qubit depending on two control qubits specified by the user.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_ccx.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-SWAP:

Gate SWAP
#########

|   **Input:** Quantum circuit, index of a first qubit, index of second qubit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the SWAP gate on two qubits.
|
|   **Description:** The SWAP gate is two-qubit operation. 
|   Expressed in basis states, the SWAP gate swaps the state of the two qubits involved in the operation.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_swap.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|


.. _gate-CSWAP:

Gate CSWAP
##########

|   **Input:** Quantum circuit, index of a first qubit, index of second qubit, index of the control qubit
|   **Output:** Quantum Circuit
|
|   **Usage:** Applies the CSWAP gate on two qubits depending on a control qubit given by the user.
|
|   **Description:** The CSWAP gate is two-qubit operation. 
|   Expressed in basis states, the CSWAP gate swaps the state of the two qubits involved in the operation depending on a control qubit.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/nodes/gate_cswap.png
    :width: 60%
    :alt: Quantum gate 
    :align: center
    :class: img-rounded
    
|