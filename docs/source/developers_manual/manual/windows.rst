Windows
=======


#. :ref:`install-dependencies-windows-contrib-manual`
#. :ref:`intructions-windows-contrib-manual`
#. :ref:`build-windows-contrib-manual`


.. _install-dependencies-windows-contrib-manual:

Install dependencies
####################


.. important::
    Make sure to install the dependencies in the right anaconda environment.


|   ``pip install -r requirements.txt``

.. _intructions-windows-contrib-manual:

Contribute
##########


.. note::
    Click `here <https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html>`_ to learn about the forking workflow on Gitlab.


* Fork the repository: https://gitlab.com/quantum-creative-group/quantum_nodes_manual
* Do your modifications
* Once you are ready, open a new `merge request <https://gitlab.com/quantum-creative-group/quantum_nodes_manual/-/merge_requests>`_
* Wait for your modifications to be reviewed and accepted

.. _build-windows-contrib-manual:

Build the manual
################

* Clone the repository next to the `quantum_nodes` repository.

*   |   Open a terminal and enter: ``make html spelling``
    |   Visualize the html in ``build/html``