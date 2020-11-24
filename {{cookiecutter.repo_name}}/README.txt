{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd {{ cookiecutter.repo_name }}

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

{% if cookiecutter.backend == 'sqlalchemy' -%}
- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_{{ cookiecutter.repo_name }}_db development.ini

{% endif -%}
- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
