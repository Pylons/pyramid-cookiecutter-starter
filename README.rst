============================
pyramid-cookiecutter-starter
============================

A cookiecutter (project template) for creating a Pyramid starter project using Chameleon for templating.

Requirements
------------

* Python 2.7 or 3.3+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Pyramid project.

.. code-block:: bash

    $ cookiecutter https://github.com/Pylons/pyramid-cookiecutter-starter

2. Change directory to the project name given in the last cookiecutter question.

.. code-block:: bash

    $ cd my_project_name

3. Run your project.

.. code-block:: bash

    $ bin/pserve development.ini

For Python 3, a virtual environment is automatically created and set up in development mode.
