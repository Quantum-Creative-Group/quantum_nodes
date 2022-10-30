.. _install-quantum-nodes-windows:

Windows
=======


.. note::
    This tutorial helps you to install Quantum Nodes and all the necessary dependencies, from scratch.


#. :ref:`downloads-windows`
#. :ref:`install-dependencies-windows`
#. :ref:`install-addon-windows`
#. :ref:`help-windows`


.. _downloads-windows:

Downloads
#########


.. _blender-download-windows:

Blender
*******

* Download and install Blender (>= 2.92): https://www.blender.org/download/


.. _animation-nodes-download-windows:

Animation Nodes
***************

* Download the add-on from the `Github releases <https://github.com/JacquesLucke/animation_nodes/releases/tag/master-cd-build>`_
  page (latest version)

.. warning::
    Be careful when you choose the file to download.
    As `mentioned here <https://docs.blender.org/api/current/info_tips_and_tricks.html#bundled-python-extensions>`_, 
    the python version (`major and minor <https://linuxize.com/post/how-to-check-python-version/>`_) must match the one that Blender
    comes with.


.. _quantum-nodes-download-windows:

Quantum Nodes
*************

* Download the add-on from the `Github releases <https://github.com/Quantum-Creative-Group/quantum_nodes/releases>`_
  page (latest version recommended)
 

.. _install-dependencies-windows:

Install dependencies
####################

In this part, we are going to install python packages on which Quantum Nodes depends.
These packages will be installed in the python distribution shipped with Blender.

* Open a new `terminal` / `command prompt` in **administrator mode**.

*   |   Go where python is installed in the Blender files
    |   By default, the files are located here: ``C:\Program Files\Blender Foundation\...``
    |   So enter: ``cd C:\Program Files\Blender Foundation\Blender 3.2\3.2\python\bin``


Install python packages
***********************

|   Make sure we have pip installed:  ``.\python.exe -m ensurepip``

|   Install packages:
|   pip: ``.\python.exe -m pip install --upgrade --no-cache-dir pip -t ..\lib\site-packages\``
|   wheel: ``.\python.exe -m pip install --upgrade --no-cache-dir wheel -t ..\lib\site-packages\``
|   pillow: ``.\python.exe -m pip install --upgrade --no-cache-dir pillow -t ..\lib\site-packages\``
|   qiskit: ``.\python.exe -m pip install --upgrade --no-cache-dir qiskit qiskit_finance qiskit_machine_learning``


.. _install-addon-windows:

Install add-on
##############

Now, all we have to do is to install Animation Nodes and Quantum Nodes in Blender.

* Open Blender

* Go to: ``Edit > Preferences``

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.png
    :width: 50%
    :alt: Blender, preferences
    :align: center
    :class: img-rounded
    
|

* Go to the add-on panel and click on ``Install``

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.5.png
    :width: 80%
    :alt: Blender, preferences, install
    :align: center
    :class: img-rounded
    
|


.. _animation-nodes-install-blender-windows:

Animation Nodes
***************

* Select Animation Nodes

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/installation/windows/install-windows-select-animation-nodes.png
    :width: 80%
    :alt: Blender, preferences, install animation nodes
    :align: center
    :class: img-rounded
    
|

* Click on ``Install Add-on``.


.. important::
    Don't forget to activate it (click on the *checkbox*)


.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/installation/windows/install-windows-activate-animation-nodes.png
    :width: 80%
    :alt: Blender, preferences, activate animation nodes
    :align: center
    :class: img-rounded
    
|


.. _quantum-nodes-install-blender-windows:

Quantum Nodes
*************

* Select Quantum Nodes

.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/installation/windows/install-windows-select-quantum-nodes.png
    :width: 80%
    :alt: Blender, preferences, install quantum nodes
    :align: center
    :class: img-rounded
    
|

* Click on ``Install Add-on``.


.. important::
    Don't forget to activate it (click on the *checkbox*)


.. image:: https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/raw/assets/installation/windows/install-windows-activate-quantum-nodes.png
    :width: 80%
    :alt: Blender, preferences, activate quantum nodes
    :align: center
    :class: img-rounded
    
|

**The end, enjoy** |:blush:|


.. _help-windows:

Help
####

If you have any problem: 

#. Check for any existing `issue <https://github.com/Quantum-Creative-Group/quantum_nodes/issues>`_ that may tackle yours
#. If you do not find anything, please open a new `issue <https://github.com/Quantum-Creative-Group/quantum_nodes/issues>`_
   on Github with all the necessary information to help you |:wink:|