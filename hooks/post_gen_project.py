""" Enable venv and show convenience message """
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
        subprocess.check_output(
            [sys.executable, '-m', 'virtualenv', path],
            shell=WIN,
        )
elif virtualenv:
    def make_venv(path):
        venv.create(path, with_pip=True)


if VIRTUALENV_AVAILABLE:
    PIP = ['bin/python', '-m', 'pip', 'install']
    make_venv('.')
    proc = subprocess.Popen(
        PIP + ['--upgrade', 'pip', 'setuptools'],
        shell=WIN,
    )
    proc.wait()
    proc = subprocess.Popen(
        PIP + ['-e', '.[testing]'],
        shell=WIN,
    )
    proc.wait()

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
