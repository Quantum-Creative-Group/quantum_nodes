Contribute to the manual
========================


* :ref:`development-environment-contrib-manual`
* :ref:`tools-contrib-manual`
* :ref:`guidelines-contrib-manual`
* :ref:`git-workflow-contrib-manual`

.. _development-environment-contrib-manual:

Development environment
***********************


Install dependencies
--------------------


.. important::
    Make sure to install the dependencies in an appropriate python environment.
    For example, you can use the one which comes with Blender.


|   Run: ``pip install -r requirements.txt``


Contribute
----------


.. note::
    Click `here <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_ to learn about the forking workflow on Github.


* Fork the repository: https://github.com/Quantum-Creative-Group/quantum_nodes
* Do your modifications
* Once you are ready, open a new `pull request <https://github.com/Quantum-Creative-Group/quantum_nodes/pulls>`_
* Wait for your modifications to be reviewed and accepted


Build the manual
----------------

* Clone the `quantum_nodes <https://github.com/Quantum-Creative-Group/quantum_nodes>`_ repository.

*   |   Open a terminal and go in the ``docs`` folder: ``cd docs``
    |   Then type: ``make html`` (or ``make.bat html`` on Windows)
    |   Visualize the html in ``build/html``


.. _tools-contrib-manual:

Tools
*****

Here is a list of tools which will help you to write documentation.

#. :ref:`tools-vs-code-extensions`
    #. :ref:`tools-pydocstring-generator-vscode`
    #. :ref:`tools-rst-vscode`


.. _tools-vs-code-extensions:

VSCode extensions
-----------------


.. _tools-pydocstring-generator-vscode:

Python Docstring Generator
##########################


.. note::
    Automatically generates the right docstring format for methods / functions / classes ...


* Install `python docstring generator <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_

* Select the ``sphinx`` format for the auto docstring functionality

.. image:: /images/contrib-tools/docstring_format.png
    :width: 85%
    :alt: Python Docstring Generator, auto docstring sphinx
    :align: center
    :class: img-rounded

|

.. _tools-rst-vscode:

reStructuredText Syntax highlighting
####################################


.. note::
    Syntax highlighting and document symbols for reStructuredText


* Install `reStructuredText syntax highlighting <https://marketplace.visualstudio.com/items?itemName=trond-snekvik.simple-rst>`_
* This extension uses `Esbonio <https://swyddfa.github.io/esbonio/docs/latest/en/>`_
* Select the right output for sphinx-build in the settings:

.. image:: /images/contrib-tools/esbonio_output_sphinx_build.png
    :width: 85%
    :alt: reStructuredText syntax highlighting, set output path sphinx-build
    :align: center
    :class: img-rounded

|


.. _guidelines-contrib-manual:

Guidelines
**********


#. :ref:`files-architecture-contrib-manual`
#. :ref:`add-a-new-chapter-contrib-manual`


.. _files-architecture-contrib-manual:

Files architecture
------------------

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


.. _add-a-new-chapter-contrib-manual:

Add a new chapter
-----------------

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
    *   |   Once this is done, add your path to the ``html_css_files`` variable in ``config.py``

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


.. _git-workflow-contrib-manual:

Git workflow
************

.. image:: https://miro.medium.com/max/560/1*UH5ozOBwkaFhWA1mrJkVIQ.png
    :alt: Git workflow
    :align: center
    :width: 80%
    :class: img-rounded

|