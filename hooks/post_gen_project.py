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

    layout = None
    mytemplate = None
    removal_text = None
    view = os.path.join(working, '{{cookiecutter.repo_name}}', 'views.py')

    if selected_lang == 'jinja2':
        removal_text = ['chameleon', 'mytemplate.pt']
        layout = os.path.join(templates, 'layout.pt')
        mytemplate = os.path.join(templates, 'mytemplate.pt')
    elif selected_lang == 'chameleon':
        removal_text = ['jinja2']
        layout = os.path.join(templates, 'layout.jinja2')
        mytemplate = os.path.join(templates, 'mytemplate.jinja2')

    delete_files([layout, mytemplate])

    setup = os.path.join(working, 'setup.py')
    init = os.path.join(working, '{{cookiecutter.repo_name}}', '__init__.py')
    remove_lines_from_files([setup, init, view], removal_text)


def delete_files(files):
    for file in files:
        if not os.path.exists(file):
            print("WARNING: Cookiecutter post generation cannot find file: " + file)
        else:
            os.remove(file)


def remove_lines_from_files(files, substring_entries):
    for file in files:
        if not os.path.exists(file):
            print("WARNING: Post generation cannot find file: " + file)
            continue

        with open(file, mode='r') as fin:
            lines = fin.readlines()

        with open(file, mode='w') as fout:
            for line in lines:
                skip_line = False
                for substring in substring_entries:
                    if line.find(substring) >= 0:
                        skip_line = True

                if not skip_line:
                    fout.write(line)


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
        Documentation: http://docs.pylonsproject.org/projects/pyramid/en/latest/
        Tutorials:     http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
        Twitter:       https://twitter.com/trypyramid
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
