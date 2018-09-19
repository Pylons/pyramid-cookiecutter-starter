from pyramid.config import Configurator
{%- if cookiecutter.backend == 'zodb' %}
from pyramid_zodbconn import get_connection
from .models import appmaker


def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())
{%- endif %}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
    {%- if cookiecutter.backend == 'sqlalchemy' %}
        config.include('.models')
    {%- endif %}
    {%- if cookiecutter.backend == 'zodb' %}
        settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'
        config.include('pyramid_tm')
        config.include('pyramid_retry')
        config.include('pyramid_zodbconn')
        config.set_root_factory(root_factory)
    {%- endif %}
        config.include('pyramid_{{ cookiecutter.template_language }}')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
