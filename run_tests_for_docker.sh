#!/bin/bash
find /app -name '*.pyc' -delete
rm -f -R /app/__pycache__

set -o errexit # if anything fails, stops and exits with failure
pytest --cov --cov-report html -x
coverage report