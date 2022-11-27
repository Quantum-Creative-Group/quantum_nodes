.. _linux-contrib-addon:

Linux
=====

.. note::

    This tutorial will help you to setup a full development environment for ubuntu.


.. _linux-dev-env-downloads-contrib-addon:

Downloads
#########


.. _linux-dev-env-downloads-blender-contrib-addon:

Blender
*******

* | First, we need to download a portable version of Blender.
  | Download a version from here: https://www.blender.org/download/.


.. _linux-dev-env-downloads-animation-nodes-contrib-addon:

Animation Nodes
***************

* | Before downloading Animation Nodes, we need to know which python version is shipped with the
  | chosen Blender version. We can get it by looking at the files (from the archive) located
  | at: ``blender[...]/[X.Y]/python/bin/``.
  | For Blender >= 2.93.0, it will probably be something between python 3.9 and 3.10.

* | Once we know that, we have to download the add-on from the release page of
  | Animation Nodes (take latest): https://github.com/JacquesLucke/animation_nodes/releases/tag/master-cd-build.


.. _linux-dev-env-downloads-quantum-nodes-contrib-addon:

Quantum Nodes
*************

* Make a fork of the repository: https://github.com/Quantum-Creative-Group/quantum_nodes/fork.
* Then, clone the forked repository on your computer.


.. _linux-dev-env-downloads-ide-contrib-addon:

IDE
***

* We recommend to use `Visual Studio Code <https://code.visualstudio.com/>`_.
* See :ref:`tools-dev-addon` for more information.


.. _linux-dev-env-installations-contrib-addon:

Installations
#############


.. note::

    Since Blender comes with its own python environment, we will use this one as our development environment too.


.. _linux-dev-env-installations-blender-contrib-addon:

Blender
*******

* | Decompress the downloaded archive which contains the blender version.
  | We can place these files where we want. However, we recommend to place them in the ``/opt/`` folder.

* Run Blender at least one time to make sure it works fine.


.. _linux-dev-env-installations-python-contrib-addon:

Python dependencies
*******************

We need to run the installation from the python distribution of Blender. For that, we need the path to the python
executable. We can find it here: ``path/to/blender/files/ .... /[X.Y]/python/bin/python3.X``.

.. note::

    | Since we will need to reference this several times, we can add an alias in the ``.bash_aliases`` file located
    | in the ``home/[username]/`` directory (create the file if it does not exist).
    | Example: ``alias pythonb=/opt/blender-3.0.1-linux-x64/3.0/python/bin/python3.9``

* Go to the ``quantum_nodes/`` directory.
* Run ``path/to/blender/files/ .... /[X.Y]/python/bin/python3.X -m pip install -r requirements.txt``.


.. _linux-dev-env-installations-animation-nodes-contrib-addon:

Animation Nodes
***************

In this part we will install the add-on for Blender and copy the content of the ``animation_nodes/`` folder in the
blender python distribution so it will be available for our different scripts (documentation build and test suite).

Installation in Blender:

* Install the add-on inside Blender (as in the :ref:`installation guide <animation-nodes-install-blender-linux>`).
* Make sure it works fine.

Installation for the IDE and the python scripts:

* Extract the ``animation_nodes/`` folder from the archive.
* | Run the following bash script ``scripts/setup_animation_nodes.sh``. You need to provide several information in order
  | to run the script correctly.
  | -> The path to the ``site-packages/`` folder in the python distribution shipped with Blender.
  | -> The path to the ``animation_nodes/`` folder previously extracted.
  | -> The path to the ``quantum_nodes/`` folder.
  | Example:
  | ``bash scripts/setup_animation_nodes.sh /opt/blender-3.0.1-linux-x64/3.0/python/lib/python3.9/site-packages/ ~/Documents/animation_nodes/ ~/Documents/quantum_nodes/``


.. _linux-dev-env-build-and-test-contrib-addon:

Build and test
##############

.. note::

    Before following the next instructions, please install and configure the recommended Visual Studio Code
    extensions cited in :ref:`this section <tools-dev-addon>`.


.. _linux-dev-env-build-and-test-run-from-vscode-contrib-addon:

Run Quantum Nodes from Visual Studio Code
*****************************************

The `Blender Development` extension let us to quickly run Blender with the modifications made to the add-on
on which we are currently working. It runs Blender in a sort of 'debug' mode to test our add-on.

* In VSCode, hit ``ctrl + shift + p`` and type ``blender start``. Then, hit ``enter``.
* If no blender executable was previously set, follow the instructions given by the extension.
* Wait for Blender to start.
* Once ready, edit code in live and save files to apply changes (it reloads the add-on automatically).


.. _linux-dev-env-build-and-test-build-documentation-contrib-addon:

Build the documentation
***********************

Generate automatic code documentation:


.. note::

    This step is not mandatory to build the documentation. You can skip it if you don't need this part
    in your local build.


* Go in the ``quantum_nodes/docs/`` folder.
* | Run:
  | ``path/to/blender/files/ .... /[X.Y]/python/bin/sphinx-apidoc -t "_templates/" --implicit-namespaces -d 1 -f -M -T -o source/developers_manual/code/ ../quantum_nodes "/*animation_nodes/*" "/*lib/*"``
  | Next commands are optional:
  | ``sed -i "1s/.*/Code documentation/" source/developers_manual/code/quantum_nodes.rst``
  | ``sed -i "2s/.*/==================/" source/developers_manual/code/quantum_nodes.rst``

Build the documentation:

* Go in the ``quantum_nodes/docs/`` folder.
* Run: ``make html SPHINXBUILD=path/to/blender/files/ .... /[X.Y]/python/bin/sphinx-build``
* The build is then available in the following folder: ``quantum_nodes/docs/build/``.


.. _linux-dev-env-build-and-test-run-test-suite-contrib-addon:

Run the test suite
******************

* Go in the ``quantum_nodes/`` folder.
* Run: ``path/to/blender/files/ .... /[X.Y]/python/bin/python3.X -m scripts.test -b [blender version] -os [operating system]``
* Example: ``path/to/blender/files/ .... /[X.Y]/python/bin/python3.X -m scripts.test -b 3.0.0 -os ubuntu-latest``