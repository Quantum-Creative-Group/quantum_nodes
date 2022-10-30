.. _install-quantum-nodes-linux:

Linux
=====


.. important::
    This tutorial is written for Ubuntu


.. note::
    This tutorial helps you to install Quantum Nodes and all the necessary dependencies, from scratch.


#. :ref:`downloads-linux`
#. :ref:`install-dependencies-linux`
#. :ref:`install-addon-linux`
#. :ref:`help-linux`


.. _downloads-linux:

Downloads
#########


.. _blender-download-linux:

Blender
*******

* Download Blender (>= 2.93): https://www.blender.org/download/


.. _blender-install-linux:

Install
-------

* You can unzip the downloaded file in ``/opt``.

* Or you can install Blender using ``sudo apt install blender``. But this won't let you
  choose the version.


.. _animation-nodes-download-linux:

Animation Nodes
***************

* Download the add-on from the `Github releases <https://github.com/JacquesLucke/animation_nodes/releases/tag/master-cd-build>`_
  page (latest version)

.. warning::
    Be careful when you choose the file to download.
    As `mentioned here <https://docs.blender.org/api/current/info_tips_and_tricks.html#bundled-python-extensions>`_, 
    the python version (`major and minor <https://linuxize.com/post/how-to-check-python-version/>`_) must match the one that Blender
    comes with.


.. _quantum-nodes-download-linux:

Quantum Nodes
*************

* Download the add-on from the `Github releases <https://github.com/Quantum-Creative-Group/quantum_nodes/releases>`_
  page (latest version recommended)
 

.. _install-dependencies-linux:

Install dependencies
####################

In this part, we are going to install python packages on which Quantum Nodes depends.
These packages will be installed in the python distribution shipped with Blender.

* Open a new `terminal`.

*   |   Go where python is installed in the Blender files
    |   If installed under ``/opt``, the files are located here: ``/opt/blender-3.2.0-linux-x64/...``
    |   So enter: ``cd /opt/blender-3.2.0-linux-x64/3.2/python/bin``


Install python packages
***********************


.. important::
    Be sure to run commands with ``sudo``.


|   Make sure we have pip installed:  ``sudo ./python3.10 -m ensurepip``

|   Install packages:
|   pip: ``sudo ./python3.10 -m pip install --upgrade --no-cache-dir pip -t ..\lib\site-packages``
|   wheel: ``sudo ./python3.10 -m pip install --upgrade --no-cache-dir wheel -t ..\lib\site-packages``
|   pillow: ``sudo ./python3.10 -m pip install --upgrade --no-cache-dir pillow -t ..\lib\site-packages``
|   qiskit: ``sudo ./python3.10 -m pip install --upgrade --no-cache-dir qiskit qiskit_finance qiskit_machine_learning``


.. _install-addon-linux:

Install add-on
##############

Now, all we have to do is to install Animation Nodes and Quantum Nodes in Blender.

* Open Blender

* Go to: ``Edit > Preferences``

.. image:: /images/installation/linux/preferences-blender-linux.png
    :width: 50%
    :alt: Blender, preferences
    :align: center
    :class: img-rounded
    
|

* Go to the add-on panel and click on ``Install``

.. image:: /images/installation/linux/install-addons-blender-linux.png
    :width: 80%
    :alt: Blender, preferences, install
    :align: center
    :class: img-rounded
    
|


.. _animation-nodes-install-blender-linux:

Animation Nodes
***************

* Select Animation Nodes

.. image:: /images/installation/linux/install-linux-select-animation-nodes.png
    :width: 80%
    :alt: Blender, preferences, install animation nodes
    :align: center
    :class: img-rounded
    
|

* Click on ``Install Add-on``.


.. important::
    Don't forget to activate it (click on the *checkbox*)


.. image:: /images/installation/linux/install-linux-activate-animation-nodes.png
    :width: 80%
    :alt: Blender, preferences, activate animation nodes
    :align: center
    :class: img-rounded
    
|


.. _quantum-nodes-install-blender-linux:

Quantum Nodes
*************

* Select Quantum Nodes

.. image:: /images/installation/linux/install-linux-select-quantum-nodes.png
    :width: 80%
    :alt: Blender, preferences, install quantum nodes
    :align: center
    :class: img-rounded
    
|

* Click on ``Install Add-on``.


.. important::
    Don't forget to activate it (click on the *checkbox*)


.. image:: /images/installation/linux/install-linux-activate-quantum-nodes.png
    :width: 80%
    :alt: Blender, preferences, activate quantum nodes
    :align: center
    :class: img-rounded
    
|

**The end, enjoy** |:blush:|


.. _help-linux:

Help
####

If you have any problem: 

#. Check for any existing `issue <https://github.com/Quantum-Creative-Group/quantum_nodes/issues>`_ that may tackle yours
#. If you do not find anything, please open a new `issue <https://github.com/Quantum-Creative-Group/quantum_nodes/issues>`_
   on Github with all the necessary information to help you |:wink:|