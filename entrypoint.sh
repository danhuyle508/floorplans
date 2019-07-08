#!/bin/bash
set -e

cd /src

# python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000