# Ensure that python3 is installed

## single command install
git clone [https://github.com/imasif/coding_test.git](https://github.com/imasif/coding_test.git) && cd coding_test && sudo chmod +x main.sh && ./main.sh

## Manual install

> git clone [https://github.com/imasif/coding_test.git](https://github.com/imasif/coding_test.git) && cd coding_test
> pip3 install virtualenv
> virtualenv venv
> . venv/bin/activate
> pip install -r requirements.txt
> FLASK_APP=main.py FLASK_ENV=development flask run