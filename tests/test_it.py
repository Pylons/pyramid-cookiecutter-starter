import os
import pytest
import sys
import subprocess

WIN = sys.platform == 'win32'

@pytest.fixture
def venv(tmpdir):
    venv = VirtualEnvironment(tmpdir.strpath)
    venv.create()
    yield venv


class VirtualEnvironment(object):
    def __init__(self, path):
        self.path = path
        self.bin = os.path.join(
            self.path,
            'bin' if sys.platform != 'win32' else 'Scripts',
        )
        self.python = os.path.join(self.bin, 'python')

    def create(self):
        subprocess.check_call(
            [sys.executable, '-m', 'virtualenv', self.path],
        )

    def install(self, pkg_name, editable=False, cwd=None):
        cmd = [self.python, '-m', 'pip', 'install']
        if editable:
            cmd += ['-e']
        cmd += [pkg_name]
        subprocess.check_call(cmd, cwd=cwd)


def test_it(cookies, venv, capfd):
    result = cookies.bake(extra_context={
        'project_name': 'Test Project',
        'repo_name': 'myapp',
    })
    assert result.exit_code == 0
    assert result.project.basename == 'myapp'

    out, err = capfd.readouterr()
    if WIN:
        assert 'Scripts\\pserve' in out
    else:
        assert 'bin/pserve' in out

    cwd = result.project.strpath
    venv.install('.[testing]', editable=True, cwd=cwd)
    subprocess.check_call([venv.python, '-m', 'pytest', '-q'], cwd=cwd)


def test_it_invalid_module_name(cookies, venv, capfd):
    result = cookies.bake(extra_context={
        'repo_name': '0invalid',
    })
    assert result.exit_code == -1
