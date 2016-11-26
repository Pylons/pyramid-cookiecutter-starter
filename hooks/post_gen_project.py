import os
import subprocess
import sys

from textwrap import dedent

WIN = sys.platform.startswith('win')

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

    Create a virtual environment for the project:
        cd {{ cookiecutter.repo_name }}
        %(venv_cmd)s %(venv)s

    Install the project into the virtual environment:
        %(pip_cmd)s install -e ".[testing]"

    To run the generated application:
        %(pserve_cmd)s development.ini
    """ % vars)
print(msg)
