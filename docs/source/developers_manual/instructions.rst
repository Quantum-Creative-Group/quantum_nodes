.. _instructions-contrib-addon:

Instructions
============

.. note::

    This tutorial will help you to setup a full development environment.


#. :ref:`dev-env-downloads-contrib-addon`
#. :ref:`dev-env-installations-contrib-addon`
#. :ref:`dev-env-build-and-test-contrib-addon`
#. :ref:`guidelines-contrib-manual`

Glossary
########

#. | ``pythonblender``: path to python executable which comes with blender.
   | Example: ``C:\Users\felix\Documents\blender-3.0.1-windows-x64\3.0\python\bin\python.exe``.
#. | ``sphinx-apidoc``: path to sphinx-apidoc executable.
   | Example: ``C:\Users\felix\AppData\Roaming\Python\Python39\Scripts\sphinx-apidoc``.
#. | ``sphinx-build``: path to sphinx-build executable.
   | Example: ``C:\Users\felix\AppData\Roaming\Python\Python39\Scripts\sphinx-build``.

.. _dev-env-downloads-contrib-addon:

Downloads
#########


.. _dev-env-downloads-blender-contrib-addon:

Blender
*******

* | First, we need to download a portable version of Blender.
  | Download a version from here: https://download.blender.org/release/.


.. _dev-env-downloads-animation-nodes-contrib-addon:

Animation Nodes
***************

* | Before downloading Animation Nodes, we need to know which python version is shipped with the
  | chosen Blender version. We can get it by looking at the files (from the archive) located
  | at: ``blender[...]/[X.Y]/python/bin/``.
  | For Blender >= 2.93.0, it will probably be something between python 3.9 and 3.10.

* | Once we know that, we have to download the add-on from the release page of
  | Animation Nodes (take latest): https://github.com/JacquesLucke/animation_nodes/releases/tag/master-cd-build.


.. _dev-env-downloads-quantum-nodes-contrib-addon:

Quantum Nodes
*************

* Make a fork of the repository: https://github.com/Quantum-Creative-Group/quantum_nodes/fork.
* Then, clone the forked repository on your computer.


.. _dev-env-downloads-ide-contrib-addon:

IDE
***

* We recommend to use `Visual Studio Code <https://code.visualstudio.com/>`_.
* See :ref:`tools-dev-addon` for more information.


.. _dev-env-installations-contrib-addon:

Installations
#############


.. note::

    Since Blender comes with its own python environment, we will use this one as our development environment too.


.. _dev-env-installations-blender-contrib-addon:

Blender
*******

* | Decompress the downloaded archive which contains the blender version.
  | We can place these files where we want.
  | ``Linux``   : We recommend you to place them in the ``/opt/`` folder.
  | ``Windows`` : We recommend you to place them in the ``Documents/`` folder.
  | ``Mac``     : [TODO].

* Run Blender at least one time to make sure it works fine.


.. _dev-env-installations-python-contrib-addon:

Python dependencies
*******************


* Go to the ``quantum_nodes/`` directory.
* Run ``pythonblender -m pip install -r requirements.txt``.


.. _dev-env-installations-animation-nodes-contrib-addon:

Animation Nodes
***************

In this part we will install the add-on for Blender and copy the content of the ``animation_nodes/`` folder in the
blender python distribution so it will be available for our different scripts (documentation build and test suite).

Installation in Blender:

* Install the add-on inside Blender (as in the :ref:`installation guide <animation-nodes-install-blender-linux>`).
* Make sure it works fine.

Installation for the IDE and the python scripts:

* | Extract the ``animation_nodes/`` folder from the archive.
  | ``Linux``   : Run the following bash script ``scripts/setup_animation_nodes.sh``.
  | ``Windows`` : Run the following bash script ``scripts/setup_animation_nodes.ps1``.
  | ``Mac``     : [TODO]
* | You need to provide several information in order to run the script correctly:
  | -> The path to the ``site-packages/`` folder in the python distribution shipped with Blender.
  | -> The path to the ``animation_nodes/`` folder previously extracted.
  | -> The path to the ``quantum_nodes/`` folder.
  | Examples:
  | ``Linux``   : ``bash scripts/setup_animation_nodes.sh /opt/blender-3.0.1-linux-x64/3.0/python/lib/python3.9/site-packages/ ~/Documents/animation_nodes/ ~/Documents/quantum_nodes/``
  | ``Windows`` : ``scripts/setup_animation_nodes.ps1 -site_packages C:\Users\felix\Documents\blender-3.0.1-windows-x64\3.0\python\lib\site-packages\ -animation_nodes C:\Users\felix\Documents\quantum_nodes\animation_nodes - C:\Users\felix\Documents\quantum_nodes``
  | ``Mac``     : [TODO]


.. _dev-env-build-and-test-contrib-addon:

Build and test
##############

.. note::

    Before following the next instructions, please install and configure the recommended Visual Studio Code
    extensions cited in :ref:`this section <tools-dev-addon>`.


.. _dev-env-build-and-test-run-from-vscode-contrib-addon:

Run Quantum Nodes from Visual Studio Code
*****************************************

The `Blender Development` extension let us to quickly run Blender with the modifications made to the add-on
on which we are currently working. It runs Blender in a sort of 'debug' mode to test our add-on.

* In VSCode, hit ``ctrl + shift + p`` and type ``blender start``. Then, hit ``enter``.
* If no blender executable was previously set, follow the instructions given by the extension.
* Wait for Blender to start.
* Once ready, edit code in live and save files to apply changes (it reloads the add-on automatically).


.. _dev-env-build-and-test-build-documentation-contrib-addon:

Build the documentation
***********************

Generate automatic code documentation:


.. note::

    This step is not mandatory to build the documentation. You can skip it if you don't need this part
    in your local build.


* Go in the ``quantum_nodes/docs/`` folder.
* | Run: ``sphinx-apidoc -t "_templates/" --implicit-namespaces -d 1 -f -M -T -o source/developers_manual/code/ ../quantum_nodes "/*animation_nodes/*" "/*lib/*"``


Build the documentation:

* | Go in the ``quantum_nodes/docs/`` folder.
  | Run (``Linux``)   : ``make html SPHINXBUILD=sphinx-build``
  | Run (``Windows``) : ``make.bat html SPHINXBUILD=sphinx-build``
  | Run (``Mac``)     : [TODO]
* The build is then available in the following folder: ``quantum_nodes/docs/build/``.


.. _dev-env-build-and-test-run-test-suite-contrib-addon:

Run the test suite
******************

* | From root of the repository, run: ``pythonblender -m scripts.test -b [blender version] -os [operating system]``
  | Example (``Linux``)   : ``pythonblender -m scripts.test -b 3.0.0 -os ubuntu-latest``
  | Example (``Windows``) : ``pythonblender -m scripts.test -b 3.0.0 -os windows-latest``
  | Example (``Mac``)     : [TODO]


.. _guidelines-contrib-manual:

Guidelines manual
#################


File architecture
*****************

.. raw:: html

    <pre>
    docs/
    ├── _static/
    │   ├── animation_nodes_init_replacement_file.txt
    │   ├── css/
    │   └── images/
    │
    ├── _templates/
    │   ├── modules.rst_t
    │   ├── packages.rst_t
    │   └── toc.rst_t
    │
    ├── build/
    │
    ├── source/
    │   ├── conf.py
    │   ├── index.rst
    │   ├── MethodNameFilter.py
    │   ├── spelling_wordlist.txt
    │   │
    │   ├── [chapter]/
    │   │   ├── index.rst
    │   │   ├── file.rst
    │   │   ├── [subchapter]/
    │   │   ├── ...
    │   │   └── [subchapter]/
    │   │
    │   ├── ...
    │   └── [chapter]/
    │       └── ...
    │
    └── ...
    </pre><br>


Add a new chapter
*****************

#. Create a new folder
    * If your chapter is a new section, create a new folder under ``source/``
    * If your chapter is a subchapter, create a new folder under ``source/parent_chapter/``
    * Your chapter may be a subsubchapter. No problem, keep the same logic as described before
    * Give it a short and precise name (snake_case naming style)

#. Create a new ``index.rst`` file in your chapter
    * This file is the "welcome page" of your chapter
    * Here you can add links to any subchapters and so on ...

#. If you need to add custom css to your pages
    * Create a new folder under ``docs/_static/css/``
    * Give it the same name as your chapter
    * Insert your css files
    * | Once this is done, add your path to the ``html_css_files`` variable in ``config.py``

In a more visual way, here is the architecture of a section/chapter:

.. raw:: html

    <pre>
    ├── index.rst
    ├── my_subchapter/
    │   ├── index.rst
    │   ├── my_subsubchapter/
    │   ├── file.rst
    │   └── ...
    ├── file.rst
    └── ...
    </pre><br>

So, at the end, here is what the global architecture should look like

.. raw:: html

    <pre>
    docs/
    ├── _static/
    │   ├── animation_nodes_init_replacement_file.txt
    │   ├── css/
    │   └── images/
    │
    ├── _templates/
    │   ├── modules.rst_t
    │   ├── packages.rst_t
    │   └── toc.rst_t
    │
    ├── build/
    │
    ├── source/
    │   ├── conf.py
    │   ├── index.rst
    │   ├── MethodNameFilter.py
    │   ├── spelling_wordlist.txt
    │   │
    │   ├── my_chapter/
    │   │   ├── index.rst
    │   │   ├── my_subchapter/
    │   │   │   ├── index.rst
    │   │   │   ├── my_subsubchapter/
    │   │   │   ├── file.rst
    │   │   │   └── ...
    │   │   ├── file.rst
    │   │   └── ...
    │   │
    │   └── ...
    │
    └── ...
    </pre><br>