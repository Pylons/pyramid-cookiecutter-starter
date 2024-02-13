import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_{{ cookiecutter.template_language }}',
    'pyramid_debugtoolbar',
    'waitress',
    {%- if cookiecutter.backend == 'sqlalchemy' %}
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy<2',
    'transaction',
    'zope.sqlalchemy',
    {%- elif cookiecutter.backend == 'zodb' %}
    'pyramid_retry',
    'pyramid_tm',
    'pyramid_zodbconn',
    'transaction',
    'ZODB',
    {%- endif %}
]

tests_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.0',
    description='{{ cookiecutter.project_name }}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = {{ cookiecutter.repo_name }}:main',
        ],
        {%- if cookiecutter.backend == 'sqlalchemy' %}
        'console_scripts': [
            'initialize_{{ cookiecutter.repo_name }}_db={{ cookiecutter.repo_name }}.scripts.initialize_db:main',
        ],
        {%- endif %}
    },
)
