import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.repo_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)
