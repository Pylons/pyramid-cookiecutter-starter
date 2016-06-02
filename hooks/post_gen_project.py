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
    venv.create('.')
    proc = subprocess.Popen(
            ['bin/pip', 'install', '--upgrade', 'pip', 'setuptools'],
            shell=sys.platform.startswith('win'),
            cwd='.'
    )
    proc = subprocess.Popen(
            ['bin/pip', 'install', '-e'],
            shell=sys.platform.startswith('win'),
            cwd='.'
    )
    proc.wait()

separator = "=" * 79
msg = dedent(
    """
    %(separator)s
    Tutorials: http://docs.pylonsproject.org/projects/pyramid_tutorials
    Documentation: http://docs.pylonsproject.org/projects/pyramid
    Twitter (tips & updates): http://twitter.com/pylons
    Mailing List: http://groups.google.com/group/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    %(separator)s
""" % {'separator': separator})
if VIRTUALENV_AVAILABLE:
    print(msg)
else:
    print msg
