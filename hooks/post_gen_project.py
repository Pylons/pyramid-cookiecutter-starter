""" Enable venv and show convenience message """
import os
import subprocess
import sys

from textwrap import dedent

WIN = sys.platform.startswith('win')

try:
    # python 3.2+
    import venv
except ImportError:
    venv = None

try:
    # python 2.x
    import virtualenv
except ImportError:
    virtualenv = None

VIRTUALENV_AVAILABLE = venv or virtualenv

if venv:
    def make_venv(path):
        venv.create(path, with_pip=True)
elif virtualenv:
    def make_venv(path):
        execute_cmd([sys.executable, '-m', 'virtualenv', path])

def execute_cmd(args):
    subprocess.check_output(
        args,
        shell=WIN,
        cwd=os.getcwd(),
        stderr=subprocess.STDOUT,
    )

def pip_install(args):
    cmd = ['bin/python', '-m', 'pip', 'install']
    cmd += args
    execute_cmd(cmd)

if VIRTUALENV_AVAILABLE:
    make_venv('.')
    pip_install(['--upgrade', 'pip', 'setuptools'])
    pip_install(['-e', '.[testing]'])

separator = "=" * 79
msg = dedent(
    """
    %(separator)s
    Tutorials:     http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
    Documentation: http://docs.pylonsproject.org/projects/pyramid/en/latest/
    Twitter:       https://twitter.com/trypyramid
    Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    %(separator)s
""" % {'separator': separator})

if VIRTUALENV_AVAILABLE:
    msg += "\nTo run the generated application:"
    msg += "\n    cd {{ cookiecutter.repo_name }}"
    msg += "\n    bin/pserve development.ini"
print(msg)
