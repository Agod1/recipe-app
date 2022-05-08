#!/bin/bash

# docker-compose run --rm api sh -c "python manage.py test && autopep8 -i app/settings.py && flake8"
docker-compose run --rm api sh -c "python manage.py test"