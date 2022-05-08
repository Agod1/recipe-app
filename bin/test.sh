#!/bin/bash

# docker-compose run api sh -c "python manage.py test && flake8"
docker-compose run api sh -c "python manage.py test"