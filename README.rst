============================
pyramid-cookiecutter-starter
============================

.. image:: https://github.com/Pylons/pyramid-cookiecutter-starter/workflows/Build%20and%20test/badge.svg?branch=1.10-branch
    :target: https://github.com/Pylons/pyramid-cookiecutter-starter/actions?query=branch%3A1.10-branch
    :alt: 1.10-branch Branch Status

A Cookiecutter (project template) for creating a Pyramid starter project.

Customizable options upon install include choice of:

*   template language (Jinja2, Chameleon, or Mako)
*   persistent backend (none, SQLAlchemy with SQLite, or ZODB)
*   mapping of URLs to routes (if the selected persistent backend is "none" or "sqlalchemy" then URL dispatch, or if "zodb" then traversal)

Requirements
------------

*   Python 2.7 or 3.4+
*   `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Versions
--------

This cookiecutter has several branches to support new features in Pyramid or avoid incompatibilities.

*   ``latest`` aligns with the latest stable release of Pyramid, and is the default branch on GitHub.
*   ``master`` aligns with the ``master`` branch of Pyramid, and is where development takes place.
*   ``x.y-branch`` aligns with the ``x.y-branch`` branch of Pyramid.


Usage
-----

#.  Generate a Pyramid project, following the prompts from the command.

    .. code-block:: bash

        $ cookiecutter gh:Pylons/pyramid-cookiecutter-starter

    Optionally append a specific branch checkout to the command:

    .. code-block:: bash

        $ cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout master

#.  Create a virtual environment, upgrade packaging tools, and install your new project and its dependencies.
    These steps are output to the console and are written to the file in ``<my_project>/README.txt`` by the cookiecutter, and are slightly different for Windows.

    .. code-block:: bash

        # Change directory into your newly created project if not already there. Your
        # current directory should be the same as this README.txt file and setup.py.
        $ cd <my_project>
        # Create a Python virtual environment, if not already created.
        $ python3 -m venv env
        # Upgrade packaging tools.
        $ env/bin/pip install --upgrade pip setuptools
        # Install the project in editable mode with its testing requirements.
        $ env/bin/pip install -e ".[testing]"

#.  If you selected ``sqlalchemy`` as a backend, there will be additional steps in the output and ``README.txt``.

#.  Run your project's tests.

    .. code-block:: bash

        $ env/bin/pytest

#.  Run your project.

    .. code-block:: bash

        $ env/bin/pserve development.ini
