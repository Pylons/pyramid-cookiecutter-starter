import pytest
import sys
import subprocess

WIN = sys.platform == 'win32'

@pytest.mark.parametrize('pyramid_dependency', [
    ('pyramid', False),
    ('git+https://github.com/Pylons/pyramid.git@master#egg=pyramid', True),
])
def test_it(pyramid_dependency, cookies, venv, capfd):
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
    venv.install(pyramid_dependency[0], editable=pyramid_dependency[1])
    venv.install(cwd + '[testing]', editable=True)
    subprocess.check_call([venv.python, '-m', 'pytest', '-q'], cwd=cwd)


def test_it_invalid_module_name(cookies, venv, capfd):
    result = cookies.bake(extra_context={
        'repo_name': '0invalid',
    })
    assert result.exit_code == -1
