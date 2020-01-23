import sys
from pip._internal.req import parse_requirements
from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

# Check python version
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of webaio requires Python {}.{}, but you're trying to
install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


install_reqs = parse_requirements(
    'requirements.txt', session='webaio'
)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    install_requires=reqs,
)
