# {{ cookiecutter.project_name }}

## Getting Started

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this `README.md` file and `pyproject.toml`.

  ```
  cd {{ cookiecutter.repo_name }}
  ```

- Create a Python virtual environment, if not already created.

  ```
  python3 -m venv env
  ```

- Upgrade packaging tools, if necessary.

  ```
  env/bin/pip install --upgrade pip
  ```

- Install the project in editable mode with its testing requirements.

  ```
  env/bin/pip install -e ".[testing]"
  ```

{% if cookiecutter.backend == 'sqlalchemy' -%}
{% set conf_prefix = (
           '' if cookiecutter.configuration_file_type == 'ini'
           else 'alembic_' ) -%}
- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

      ```
      env/bin/alembic -c {{ conf_prefix }}development.ini revision --autogenerate -m "init"
      ```

    - Upgrade to that revision.

      ```
      env/bin/alembic -c {{ conf_prefix }}development.ini upgrade head
      ```

- Load default data into the database using a script.

  ```
  env/bin/initialize_{{ cookiecutter.repo_name }}_db {{ conf_prefix }}development.ini
  ```

{% endif -%}
- Run your project's tests.

  ```
  env/bin/pytest
  ```

- Run your project.

  ```
  env/bin/pserve development.{{ cookiecutter.configuration_file_type }}
  ```
