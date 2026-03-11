import os
from pyramid.paster import get_appsettings
from pyramid.scripting import prepare
from pyramid.testing import DummyRequest, testConfig
import pytest
import transaction
import webtest

from {{ cookiecutter.repo_name }} import main


def pytest_addoption(parser):
    {%- if cookiecutter.configuration_file_type == 'ini' %}
    parser.addoption('--ini', action='store', metavar='INI_FILE')
    {%- else %}
    parser.addoption('--yaml', action='store', metavar='YAML_FILE')
    {%- endif %}    

@pytest.fixture(scope='session')
def {{ cookiecutter.configuration_file_type }}_file(request):
    # potentially grab this path from a pytest option
    return os.path.abspath(request.config.option.{{ cookiecutter.configuration_file_type }} or 'testing.{{ cookiecutter.configuration_file_type }}')

@pytest.fixture(scope='session')
def app_settings({{ cookiecutter.configuration_file_type }}_file):
    return get_appsettings({{ cookiecutter.configuration_file_type }}_file)

@pytest.fixture(scope='session')
def app(app_settings):
    return main({}, **app_settings)

@pytest.fixture
def tm():
    tm = transaction.manager
    tm.begin()
    tm.doom()

    yield tm

    tm.abort()

@pytest.fixture
def testapp(app, tm):
    testapp = webtest.TestApp(app, extra_environ={
        'HTTP_HOST': 'example.com',
        'tm.active': True,
        'tm.manager': tm,
    })

    return testapp

@pytest.fixture
def app_request(app, tm):
    """
    A real request.

    This request is almost identical to a real request but it has some
    drawbacks in tests as it's harder to mock data and is heavier.

    """
    with prepare(registry=app.registry) as env:
        request = env['request']
        request.host = 'example.com'
        yield request

@pytest.fixture
def dummy_request(tm):
    """
    A lightweight dummy request.

    This request is ultra-lightweight and should be used only when the request
    itself is not a large focus in the call-stack.  It is much easier to mock
    and control side-effects using this object, however:

    - It does not have request extensions applied.
    - Threadlocals are not properly pushed.

    """
    request = DummyRequest()
    request.host = 'example.com'
    request.tm = tm

    return request

@pytest.fixture
def dummy_config(dummy_request):
    """
    A dummy :class:`pyramid.config.Configurator` object.  This allows for
    mock configuration, including configuration for ``dummy_request``, as well
    as pushing the appropriate threadlocals.

    """
    with testConfig(request=dummy_request) as config:
        yield config
