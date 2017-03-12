from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
@view_config(route_name='home', renderer='templates/mytemplate.pt')
@view_config(route_name='home', renderer='/mytemplate.mako')
def my_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}
