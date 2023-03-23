#!/bin/bash

python -m pip install --upgrade pip

pip install virtualenvwrapper-win
mkvirtualenv burger_point
workon burger_point

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver --settings=burger_point.settings.prod
