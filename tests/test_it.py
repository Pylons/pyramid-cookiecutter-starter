import pytest

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
