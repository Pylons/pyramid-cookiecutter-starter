import os
import pytest
import subprocess

@pytest.fixture
def context():
    return {
        'project_name': 'Test Project',
        'repo_name': 'myapp',
    }

def test_it(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.project.basename == 'myapp'

    subprocess.check_output(
        [os.path.join('bin', 'python'), '-m', 'pytest'],
        stderr=subprocess.STDOUT,
        cwd=result.project.strpath,
    )
