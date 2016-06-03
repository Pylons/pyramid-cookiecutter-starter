""" Enable venv and show convenience message """
import subprocess
import sys

from textwrap import dedent

try:
    # python 3.2+
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


if VIRTUALENV_AVAILABLE:
    venv.create('.', with_pip=True)
    proc = subprocess.Popen(
            ['bin/pip', 'install', '--upgrade', 'pip', 'setuptools'],
            shell=sys.platform.startswith('win'),
            cwd='.'
    )
    proc.wait()
    proc = subprocess.Popen(
            ['bin/pip', 'install', '-e', '.'],
            shell=sys.platform.startswith('win'),
            cwd='.'
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
    msg += "\nTo run the generated application, cd to %s and run:" % (
        '{{ cookiecutter.repo_name }}')
    msg += "\nbin/pserve development.ini"
print(msg)
