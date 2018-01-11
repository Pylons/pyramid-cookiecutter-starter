import os
import sys
from textwrap import dedent

WIN = sys.platform.startswith('win')


def main():
    clean_unused_template_settings()
    display_actions_message()


def clean_unused_template_settings():
    selected_lang = '{{ cookiecutter.template_language }}'
    working = os.path.abspath(os.path.join(os.path.curdir))
    templates = os.path.join(working, '{{cookiecutter.repo_name}}', 'templates')

    if selected_lang == "chameleon":
        extension = ".pt"
    else:
        extension = "." + selected_lang
    delete_other_ext(templates, extension)


def delete_other_ext(directory, extension):
    """
    Removes all files not ending with the extension.
    """
    for i in os.listdir(directory):
        if not i.endswith(extension):
            os.unlink(os.path.join(directory, i))


def display_actions_message():
    venv = 'env'
    if WIN:
        venv_cmd = 'py -3 -m venv'
        venv_bin = os.path.join(venv, 'Scripts')
    else:
        venv_cmd = 'python3 -m venv'
        venv_bin = os.path.join(venv, 'bin')

    vars = dict(
        separator='=' * 79,
        venv=venv,
        venv_cmd=venv_cmd,
        pip_cmd=os.path.join(venv_bin, 'pip'),
        pytest_cmd=os.path.join(venv_bin, 'pytest'),
        pserve_cmd=os.path.join(venv_bin, 'pserve'),
    )
    msg = dedent(
        """
        %(separator)s
        Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
        Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
        Twitter:       https://twitter.com/PylonsProject
        Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
        Welcome to Pyramid.  Sorry for the convenience.
        %(separator)s

        Change directory into your newly created project.
            cd {{ cookiecutter.repo_name }}

        Create a Python virtual environment.
            %(venv_cmd)s %(venv)s

        Upgrade packaging tools.
            %(pip_cmd)s install --upgrade pip setuptools

        Install the project in editable mode with its testing requirements.
            %(pip_cmd)s install -e ".[testing]"

        Run your project's tests.
            %(pytest_cmd)s

        Run your project.
            %(pserve_cmd)s development.ini
        """ % vars)
    print(msg)


if __name__ == '__main__':
    main()
