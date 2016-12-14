import os
import pytest
import sys
import subprocess

WIN = sys.platform == 'win32'


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

    # this is a hook for executing scaffold tests against a specific
    # version of pyramid (or a local checkout on disk)
    if 'OVERRIDE_PYRAMID' in os.environ:  # pragma: no cover
        venv.install(os.environ['OVERRIDE_PYRAMID'], editable=True)

    venv.install(cwd + '[testing]', editable=True)
    subprocess.check_call([venv.python, '-m', 'pytest', '-q'], cwd=cwd)


def test_it_invalid_module_name(cookies, venv, capfd):
    result = cookies.bake(extra_context={
        'repo_name': '0invalid',
    })
    assert result.exit_code == -1
