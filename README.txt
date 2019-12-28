#Ensure that python3 is installed
> pip3 install virtualenv
> git clone  .. && cd ..
> virtualenv venv
> . venv/bin/activate
> cd code && FLASK_APP=main.py FLASK_ENV=development flask run