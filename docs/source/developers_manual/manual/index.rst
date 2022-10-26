Contribute to the manual
========================


.. _dev-env-contrib-manual:

Development environment
***********************

.. toctree::
    :maxdepth: 1

    linux
    windows
    mac
    tools


.. _intructions-linux-contrib-manual:

Contribute
**********


.. note::
    Click `here <https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html>`_ to learn about the forking workflow on Gitlab.


* Fork the repository: https://gitlab.com/quantum-creative-group/quantum_nodes_manual
* Do your modifications
* Once you are ready, open a new `merge request <https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/merge_requests>`_
* Wait for your modifications to be reviewed and accepted


.. _guidelines-contrib-addon:

Guidelines
**********


#. :ref:`files-architecture-contrib-manual`
#. :ref:`add-a-new-chapter-contrib-manual`


.. _files-architecture-contrib-manual:

Files architecture
------------------

.. raw:: html

    <pre>
    quantum_nodes_manual/
    ├── build/
    ├── source/
    │   ├── _static/
    │   │   └── css/
    │   │
    │   ├── conf.py
    │   ├── index.rst
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
    * If your chapter is a subchapter, create a new folder  under ``source/parent_chapter/``
    * Your chapter may be a subsubchapter. No problem, keep the same logic as described before
    * Give it a short and precise name (snake_case naming style)

#. Create a new ``index.rst`` file in your chapter
    * This file is the "welcome page" of your chapter
    * Here you can add links to any subchapters and so on ...

#. If you need to add custom css to your page.s
    * Create a new folder under ``source/_static/css/``
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
    quantum_nodes_manual/
    ├── build/
    ├── source/
    │   ├── _static/
    │   │   └── css/
    │   │       ├── ...
    │   │       └── my_chapter/
    │   │           ├── my_css_file.css
    │   │           └── ...
    │   │
    │   ├── conf.py
    │   ├── index.rst
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