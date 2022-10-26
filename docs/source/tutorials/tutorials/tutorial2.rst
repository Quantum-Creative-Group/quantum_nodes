Tutorial 2 - Use a quantum circuit to modify a mesh
===================================================


|   In this tutorial, we are going to use results from a quantum circuit to modify a mesh in Blender.

    * :ref:`convert-in-floats`
    * :ref:`access-vertices`
    * :ref:`modify-vertices`
    * :ref:`number-floats`

|   To begin, we are going to modify a cube.

*   |   First, we will create a quantum circuit (if you need help, check the tutorial 1).


.. _convert-in-floats:

1 - Convert quantum result in floats
####################################

|   Here, we want to be able to modify all vertices of the cube, so we will need 8 results, that means we will need 3 qubits (2^3 = 8). 
|   We are only going to use the state-vector of the circuit, so we don't need a classical register.

Let's create the following circuit:

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step1.png
    :width: 85%
    :alt: Step 1 
    :align: center
    :class: img-rounded

|

|   Here we have the state-vector with probabilities related to qubits. 
|   To send the complex list from the state-vector, we will create a group that contains our circuit and send this list as output.
|   To do it we use **Subprograms** options from **Animation Nodes**.

|   Let's create the Quantum Circuit group:

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step2.png
    :width: 85%
    :alt: Step 2 
    :align: center
    :class: img-rounded

|

|   To use complexes, we will need to convert our output into floats. 
|   To do that, Quantum Nodes implements a node **Split Complex128** that returns float from the real part and the imaginary part of the complex number.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step3.png
    :width: 85%
    :alt: Step 3
    :align: center
    :class: img-rounded

|

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step4.png
    :width: 85%
    :alt: Step 4
    :align: center
    :class: img-rounded

|


.. note::
    This node only takes one complex at a time, so to convert all of them we will create a loop with Subprograms.


*   |   Create a new node tree and create a loop with an input taking Complex128.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step5.png
    :width: 85%
    :alt: Step 5
    :align: center
    :class: img-rounded

|

*   |   Link this node to the node **Split complex128**.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step6.png
    :width: 85%
    :alt: Step 6
    :align: center
    :class: img-rounded

|

*   |   Finally, create two outputs giving the real part and the imaginary part by clicking on New Generator Output in **Loop Input** and choosing Float List.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step7.png
    :width: 85%
    :alt: Step 7
    :align: center
    :class: img-rounded

|

|   Now we can split all complexes from a list. 


.. _access-vertices:

2 - Access the mesh vertices
############################

|   Next we are going to create our main node tree to modify our cube.

*   |   Create a new node tree.

|   In this one, we will use nodes from Animation Nodes to get vertices from an object and send back all the vertices transformed with our previous trees.

*   |   First, call the object with **Object Input** and get his vertices with **Mesh Object Input**.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step8.png
    :width: 85%
    :alt: Step 8
    :align: center
    :class: img-rounded

|

|   To be able to modify vertices from the object, we are going to get all vectors from the vertex locations and separate them to modify the axes independently.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step9.png
    :width: 85%
    :alt: Step 9
    :align: center
    :class: img-rounded

|

*   |   Go to the 3D Viewport and create a new cube. 
*   |   Use the eyedropper tool from the **Object Input** node and select the cube. This is how you choose what object the tree and therefore the quantum circuit will be applied to.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step10.png
    :width: 85%
    :alt: Step 10
    :align: center
    :class: img-rounded

|


..  note::
    |   It is really useful to split your Blender workspace in multiple screens as you will often have to move through menus. 
    |   To do that, click on a corner of one workspace and slide it. You cn then choose what kind of workspace you want it to be in the dropdown menu at the top. 


|   If you use the Viewer node, you can see the vertex locations of the cube. 
|   For example we can see all floats x from vectors.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step11.png
    :width: 85%
    :alt: Step 11
    :align: center
    :class: img-rounded

|

|   We now have access to the cube vertices.
|   We can use our quantum circuit and our loop to change them.


.. _modify-vertices:

3 - Modify vertices
###################

*   |   We use **Invoke Subprogram** to call our quantum circuit and our loop and link them to get two float lists. 

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step12.png
    :width: 85%
    :alt: Step 12
    :align: center
    :class: img-rounded

|

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step13.png
    :width: 85%
    :alt: Step 13
    :align: center
    :class: img-rounded

|

|   We can now change how we want the x, y or z list by using the node **Float Math**. 

|   For example I can choose to only change the x list by adding the real list and combine a new vector.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step14.png
    :width: 85%
    :alt: Step 14
    :align: center
    :class: img-rounded

|

*   |   We need to send our new vector to the cube again by using the **Mesh Object Output** node and select the type vertices.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step15.png
    :width: 85%
    :alt: Step 15
    :align: center
    :class: img-rounded

|

|   We can see that some vertices from our cube have been moved along the x-axis. 
 
.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step16.png
    :width: 50%
    :alt: Step 16
    :align: center
    :class: img-rounded

|
 
.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step17.png
    :width: 50%
    :alt: Step 17
    :align: center
    :class: img-rounded

|

|   You now know how to modify vertices thanks to a quantum circuit, but this way works only if you use the exact number of floats.
|   Here we use 3 qubits to obtain 8 results, it's perfect for a cube that has 8 vertices.
|   However, by increasing the number of qubits in the quantum circuit, we will have too many results.

Example if we to change to have 4 qubits:

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step18.png
    :width: 85%
    :alt: Step 18
    :align: center
    :class: img-rounded

|


.. _number-floats:

4 - Have the perfect number of floats
#####################################

|   As we've seen, Qubits give us 2^n results (n number of qubits).
|   We need to find a way to filter only the number of results we want.

|   To do that, we are going to create an adapter.

*   |   Create a new node tree and create a new Loop with the **Subprograms** menu. 

|   In parameters, we will take a float list for the real part of complex numbers. 
|   We will get the float in the list related to the index and repeat the loop until the iteration number is equal to the number of vertices.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step19.png
    :width: 85%
    :alt: Step 19
    :align: center
    :class: img-rounded

| 

|   We can use this loop in our main tree with **Invoke subprogram**. 
|   To use it correctly, we have to input the float list from the quantum circuit and specify the number of iteration with the number of vertices.

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/tutorial2/step20.png
    :width: 85%
    :alt: Step 20
    :align: center
    :class: img-rounded

|

|   Now, no matter the number of results, we get the correct number of floats to create a new vector. 
|   For example we can replace the Cube by a Sphere with more vertices and it will still work.


.. note::
    We re-implement the new vertices to the same object. If you repeat this node, it will take each time the new vertex locations.


..  important::
    Automatic execution of the node tree is the default on Blender. 
    This means that the node tree is executed as much as possible. 
    As it is CPU intensive, it is recommended to change this option by deselecting Always in the Node Tree tab.