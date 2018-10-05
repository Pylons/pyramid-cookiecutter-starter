from pyramid.view import view_config


{%- if cookiecutter.backend == 'zodb' %}

from ..models import MyModel


@view_config(context=MyModel, renderer='../templates/mytemplate.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def my_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}


{%- elif cookiecutter.backend == 'sqlalchemy' %}
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='home', renderer='../templates/mytemplate.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def my_view(request):
    try:
        query = request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': '{{ cookiecutter.project_name }}'}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


{%- elif cookiecutter.backend == 'none' %}


@view_config(route_name='home', renderer='../templates/mytemplate.{{ "pt" if "chameleon" == cookiecutter.template_language else cookiecutter.template_language }}')
def my_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}


{%- endif %}
