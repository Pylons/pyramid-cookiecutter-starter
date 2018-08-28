from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/mytemplate.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def my_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}
