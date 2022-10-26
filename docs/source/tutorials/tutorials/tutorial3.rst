Tutorial 3 - Use a quantum circuit to modify the location, rotation or scale of a mesh
======================================================================================


|   In this tutorial, we are going to use results from a quantum circuit to modify the location, rotation or scale of a mesh in blender.

    * :ref:`tutorial3-quantum-circuit`
    * :ref:`tutorial3-create-vector`
    * :ref:`tutorial3-transforming-cube`

|   We are going to modify a cube.

*   |   First, we will create a quantum circuit (if you need help you can check the tutorial #1).


.. _tutorial3-quantum-circuit:

1 - The Quantum Circuit
#######################

*   |   First we need to create a Quantum circuit.

|   In this example, we are going to use the following circuit, with 2 qubits and an RX gate:

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step1.png
    :width: 85%
    :alt: Step 1 
    :align: center
    :class: img-rounded
    
|

|   In order to ease the readability of our tree as we did in the last tutorial, we are going to put this circuit into a group so we can use it later as a subprogram.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step2.png
    :width: 50%
    :alt: Step 2
    :align: center
    :class: img-rounded
    
|


.. _tutorial3-create-vector:

2 - Create Vector
#################

*   |   Once we have our **Quantum Circuit Output**, we need to create a vector out of it. 

|   To use the data from our Quantum Circuit, we will need to convert the complex list returned to a float list.

*   |   For this, we are going to create the same subprogram as we saw in the first part of Tutorial #2.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step3.png
    :width: 85%
    :alt: Step 3
    :align: center
    :class: img-rounded
    
|

*   |   Once this is done, we can go back to creating our new group: **Create Vector**.

|   The goal of this group is to transform the results we got with our quantum circuit into a vector. 

*   |   First we are going to create our group and link our two subprograms Quantum Circuit and Complex into float, just like this:

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step4.png
    :width: 85%
    :alt: Step 4
    :align: center
    :class: img-rounded
    
|

*   |   Then we retrieve the values we want from the float list thanks to the Get List Element node and insert it into the vector that we are going to return.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step5.png
    :width: 85%
    :alt: Step 5
    :align: center
    :class: img-rounded
    
|

|   There are several ways you can create your vector. It is really up to you. 
|   Her, what we did was to use the first three floats of the list and put them respectively as the X, Y and Z of the vector. 
|   Then we multiplied their value thanks to math nodes in order for the cube to move more.


.. _tutorial3-transforming-cube:

3 - Transforming the cube 
#########################

|   Once you have your vector ready, the only thing left to do is to use it to transform your cube.

*   |   Let's create a new node tree for that.

|   We are going to use the **Object Transforms Output** node, which basically allows us to set the location, rotation and scale of a selected object to the input transformations.

|   Hence, we need to select our object as well as the transformation we want to apply to it.

*   |   Then we need to get our vector from the Create Vector Subprogram and link it to our transform Node.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step6.png
    :width: 85%
    :alt: Step 6
    :align: center
    :class: img-rounded
    
|

*   |   For example, here we are using the location transform on all axes on a cube. It is the easiest case.

|   Once you've linked it, you should see your object moving when the node tree is executed.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step7.png
    :width: 30%
    :alt: Step 7
    :class: img-rounded
.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step8.png
    :width: 30%
    :alt: Step 8
    :class: img-rounded
.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step9.png
    :width: 30%
    :alt: Step 9
    :class: img-rounded

|   It is the same principle for scaling. 

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step10.png
    :width: 85%
    :alt: Step 10
    :align: center
    :class: img-rounded

|

|   Here is the result:


.. note::
    |   Be careful not to activate the parameters if they are always at zero, else your cube will disappear.


.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step11.png
    :width: 47%
    :alt: Step 11
    :class: img-rounded
.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial3/step12.png
    :width: 47%
    :alt: Step 12
    :class: img-rounded