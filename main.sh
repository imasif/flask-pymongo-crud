#!/bin/bash
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=main.py FLASK_ENV=development flask run