#!/bin/bash

# python -m pip install --upgrade pip

# pip install virtualenvwrapper-win
# mkvirtualenv burger_point
# workon burger_point

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver --settings=burger_point.settings.prod
