from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def notfound_view(request):
    request.response.status = 404
    return {}
