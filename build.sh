#!/bin/bash

pip install -r requirement.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver --settings=burger_point.settings.prod
