============================
pyramid-cookiecutter-starter
============================

.. image:: https://travis-ci.org/Pylons/pyramid-cookiecutter-starter.png?branch=master
        :target: https://travis-ci.org/Pylons/pyramid-cookiecutter-starter
        :alt: Master Travis CI Status

A cookiecutter (project template) for creating a Pyramid starter project using
Chameleon for templating.

Requirements
------------

* Python 2.7 or 3.4+
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Pyramid project.

.. code-block:: bash

    $ cookiecutter https://github.com/Pylons/pyramid-cookiecutter-starter

2. Finish configuring the project by creating a virtual environment and
   installing your new project. These steps are output as part of the
   cookiecutter command above and are slightly different for Windows.

.. code-block:: bash

    $ cd myproj
    $ python3 -m venv env
    $ env/bin/pip install -e ".[testing]"

3. Run your project.

.. code-block:: bash

    $ env/bin/pserve development.ini
