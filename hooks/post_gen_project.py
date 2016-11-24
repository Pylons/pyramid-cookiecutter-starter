""" Enable venv and show convenience message """
import os
import subprocess
import sys

from textwrap import dedent

WIN = sys.platform.startswith('win')

venv = 'env'
if WIN:
    venv_cmd = 'py -3 -m venv'
else:
    venv_cmd = 'python3 -m venv'

vars = dict(
    separator='=' * 79,
    venv_cmd=venv_cmd,
    venv=venv,
)
msg = dedent(
    """
    %(separator)s
    Tutorials:     http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
    Documentation: http://docs.pylonsproject.org/projects/pyramid/en/latest/
    Twitter:       https://twitter.com/trypyramid
    Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    %(separator)s

    Create a virtualenv for the project:
        cd {{ cookiecutter.repo_name }}
        %(venv_cmd)s %(venv)s

    Install the project into the virtualenv:
        %(venv)s/bin/pip install -e .[testing]

    To run the generated application:
        %(venv)s/bin/pserve development.ini
    """ % vars)
print(msg)
