#!/bin/bash


echo "Starting build script"
pip install -r requirements.txt
echo "Collect static files"
python3 manage.py collectstatic --noinput --clear
echo "Build script finished"
