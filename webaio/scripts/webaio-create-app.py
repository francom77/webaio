#!/usr/bin/env python
import os
import sys

from cookiecutter.main import cookiecutter
TEMPLATE_URL = 'https://github.com/francom77/webaio-app-template.git'

try:
    os.chdir('apps')
except FileNotFoundError:
    sys.stderr.write('ERROR: There is not apps directory \n')
else:
    cookiecutter(TEMPLATE_URL)
