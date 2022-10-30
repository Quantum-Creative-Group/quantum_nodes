Tutorial 1 - Create a quantum circuit
=====================================


|   In this tutorial, we are going to use Quantum Nodes to create our first quantum circuit in Blender and see what we can use with it.

    * :ref:`tutorial1-initialize`
    * :ref:`tutorial1-gates`
    * :ref:`tutorial1-output`


.. _tutorial1-initialize:

1 - Initialize a quantum circuit
################################

*   First, open the Animation-Nodes window and create a new node tree.

.. image:: /images/tutorial1/step1.png
    :width: 85%
    :alt: Step 1 
    :align: center
    :class: img-rounded
    
|

.. image:: /images/tutorial1/step2.png
    :width: 85%
    :alt: Step 2 
    :align: center
    :class: img-rounded
    
|

*   In the Animation nodes panel, we can use nodes from Animation Nodes and Quantum Nodes. Press Shift+A to open the Animation Nodes menu or click the Add menu.

.. image:: /images/tutorial1/step3.png
    :width: 85%
    :alt: Step 3
    :align: center
    :class: img-rounded
    
|

|   In this menu you can see all options from Animation Nodes. In the bottom, there is a the Quantum Nodes menu.

.. image:: /images/tutorial1/step4.png
    :width: 85%
    :alt: Step 4
    :align: center
    :class: img-rounded
    
|

|   Here, you can select all nodes from Quantum Nodes. 

|   To create a new quantum circuit, we will create 2 registers: a quantum register and a classical register.

*   In the **Init Quantum Circuit** menu, select **Init Classical register** and **Init Quantum register**.

.. image:: /images/tutorial1/step5.png
    :width: 85%
    :alt: Step 5
    :align: center
    :class: img-rounded
    
|

|   We now have 2 registers.
|   You can choose the number of qubits and bits you want to use.

.. image:: /images/tutorial1/step6.png
    :width: 50%
    :alt: Step 6
    :align: center
    :class: img-rounded
    
|

|   Next, let's initiate our quantum circuit.

*   |   Select **Init Quantum Circuit** -> **Init Quantum Circuit**.

.. image:: /images/tutorial1/step7.png
    :width: 85%
    :alt: Step 7
    :align: center
    :class: img-rounded
    
|

|   In this node you can select if you want to initialize your circuit by input number of qubits and bits, or use registers.

.. image:: /images/tutorial1/step8.png
    :width: 85%
    :alt: Step 8
    :align: center
    :class: img-rounded
    
|

*   |   We are going to use our registers, select option “Quantum and Classical register”, and link registers to the node.

.. image:: /images/tutorial1/step9.png
    :width: 85%
    :alt: Step 9
    :align: center
    :class: img-rounded
    
|

|   Our circuit is now initialized.


.. _tutorial1-gates:

2 - Use quantum gates
#####################

|   All qubits and bits are initialized at 0. We want to change their value. 
|   Let's modify qubits by using quantum gates.

*   |   Go to the menu Quantum Gates.

.. image:: /images/tutorial1/step10.png
    :width: 85%
    :alt: Step 10
    :align: center
    :class: img-rounded
    
|

|   Here you have access to every quantum gate implemented in Quantum Nodes.


.. note::
    |   If you want to learn more about each gate implemented in Quantum Nodes, you can read our documentation `here <https://drive.google.com/file/d/1U4QceNhRnfBhOn5S-MWFM6Rzti8aVMDn/view?usp=sharing>`_.


|   For now we are going to modify one qubit.

*   |   Select **Quantum Gate X** (the NOT gate) in the **Single Qubit Gates** menu.

.. image:: /images/tutorial1/step11.png
    :width: 85%
    :alt: Step 11
    :align: center
    :class: img-rounded
    
|

*   |   To apply this gate in our circuit, you have to input the circuit in the gate and select the qubit you want to modify. 

|   You can also add the same gate to another qubit. 
|   In output we get back our circuit. 

.. image:: /images/tutorial1/step12.png
    :width: 50%
    :alt: Step 12
    :align: center
    :class: img-rounded
    
|

|   With a viewer node you can see the quantum circuit representation. 
|   Here we can see the X gate applies to the qubit 0.

.. image:: /images/tutorial1/step13.png
    :width: 85%
    :alt: Step 13
    :align: center
    :class: img-rounded
    
|

|   Now we are going to entangle two qubits by using a CX gate (Controlled NOT).

*   |   Select **Quantum Gate CX** in the **C Gates** menu and input the circuit in it.

.. image:: /images/tutorial1/step14.png
    :width: 85%
    :alt: Step 14
    :align: center
    :class: img-rounded
    
|

|   This gate entangles two qubits. 

*   |   You have to choose which qubit will control and which qubit will be the target.

.. image:: /images/tutorial1/step15.png
    :width: 85%
    :alt: Step 15
    :align: center
    :class: img-rounded
    
|

|   Now we have a circuit with multiple gates to manipulate qubits, we must be able to get results by sending them to a simulator.


.. _tutorial1-output:

3 - Get results from our quantum circuit
########################################

|   To get results from our quantum circuit, we can first measure qubits.

|   In our circuit, we created a classical register to store the qubits values. 
|   We have 2 bits in our classical register, so we only can store the value from 2 qubits (you can change the number of qubits and bits in your registers at any moment).

*   |   To store qubit values in bits we are going to use the node **Quantum Output** -> **Quantum Output** -> **Quantum Measure**

.. image:: /images/tutorial1/step16.png
    :width: 85%
    :alt: Step 16
    :align: center
    :class: img-rounded
    
|

|   With this node you can choose which qubit value will be stored in which bit. 
|   There is also an option to directly measure all qubits and automatically store them in a bit.

.. image:: /images/tutorial1/step17.png
    :width: 50%
    :alt: Step 17
    :align: center
    :class: img-rounded
    
|

.. image:: /images/tutorial1/step18.png
    :width: 50%
    :alt: Step 18
    :align: center
    :class: img-rounded
    
|

|   Here we choose to only measure the qubit 0 and 1 and store them in the bits 0 and 1. 
|   To do that use two **Quantum measure** nodes.

.. image:: /images/tutorial1/step19.png
    :width: 85%
    :alt: Step 19
    :align: center
    :class: img-rounded
    
|

|   Now that we have measured some qubits from our circuit, we are going to extract some results.


Counts 
******

*   |   First, we can get the probabilities of qubits state with the node **Quantum Circuit Get Counts** in **Quantum Output** menu.


.. important::
    A **measure node** is needed for this node to work. Add one between your circuit and the Get count node or else it won't work.


.. image:: /images/tutorial1/step20.png
    :width: 85%
    :alt: Step 20
    :align: center
    :class: img-rounded
    
|

|   This node simulates many times the circuit and returns how many times it gives the same result. 


.. note::
    In this example, we try 1024 times the circuit and get 1024 times the result “11”, which means that there is 100% chance of getting “11” as the result of this circuit.


.. image:: /images/tutorial1/step21.png
    :width: 85%
    :alt: Step 21
    :align: center
    :class: img-rounded
    
|


State vector 
************

|   In the result of a quantum circuit, you have also a state-vector that contains probabilities from qubits. 
|   These probabilities are complex numbers, so we choose with Quantum Nodes to return a complex numbers list.

*   |   To use it select **Quantum Output State**.

.. image:: /images/tutorial1/step22.png
    :width: 85%
    :alt: Step 22
    :align: center
    :class: img-rounded
    
|

|   Here we have a list of 8 complex numbers related to the number of possibilities (2^3 sequences). 

.. image:: /images/tutorial1/step23.png
    :width: 85%
    :alt: Step 23
    :align: center
    :class: img-rounded
    
|


.. note::
    In our example, we saw that there is a 100% chance to have “11” in the result. This means in the binary number that there is 100% to have 3 (11 in base 2 = 3 in base 10).


.. important::
    |   Note here that we placed the Quantum Output State after measures, it means that if you want to get the probabilities you will not be able to get them, because measures “freeze” qubits in a state. 
    |   In other words, it will return that you have 100% to get one random result and not probabilities of multiple results.


If you want probabilities you have to use Quantum Output State without measures (other example in annex)

.. image:: /images/tutorial1/step24.png
    :width: 85%
    :alt: Step 24
    :align: center
    :class: img-rounded
    
|


Other quantum circuits:
***********************

*1 Qubit, Hadamard Gate*

.. image:: /images/tutorial1/step25.png
    :width: 85%
    :alt: Step 25
    :align: center
    :class: img-rounded
    
|
    
*2 Qubits, Hadamard Gate (q0), Rotation X Gate (5°)(q1)*

.. image:: /images/tutorial1/step26.png
    :width: 85%
    :alt: Step 26
    :align: center
    :class: img-rounded
    
|

*“Bell state”: 2 Qubits, Hadamard Gate (q0), CX Gate (q0 -> q1)*

.. image:: /images/tutorial1/step27.png
    :width: 85%
    :alt: Step 27
    :align: center
    :class: img-rounded
    
|

*“Bell state” with measures*

.. image:: /images/tutorial1/step28.png
    :width: 85%
    :alt: Step 28
    :align: center
    :class: img-rounded
    
|