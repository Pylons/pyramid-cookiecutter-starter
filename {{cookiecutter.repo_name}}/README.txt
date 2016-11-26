{{ cookiecutter.project_name }}
===============================

Getting Started
---------------

- Create a Python virtual environment:

    python3 -m venv $VENV

- Install the project in editable mode:

    $VENV/bin/pip install -e ".[testing]"

- Start the server:

    $VENV/bin/pserve development.ini
