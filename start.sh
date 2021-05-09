#!/usr/bin/env bash

python3 manage.py collectstatic
python3 manage.py migrate

gunicorn FinalSite.wsgi:application -w 4 -t 600 -b 0.0.0.0:8000