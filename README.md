# Ensure that python3 is installed

> Make sure mongodb is installed served on 27017 port

## single command install
> git clone [https://github.com/imasif/coding_test.git](https://github.com/imasif/coding_test.git) && cd coding_test && sudo chmod +x main.sh && ./main.sh

## Manual install

> git clone [https://github.com/imasif/coding_test.git](https://github.com/imasif/coding_test.git) && cd coding_test

> pip3 install virtualenv

> virtualenv venv

> . venv/bin/activate

> pip install -r requirements.txt

> FLASK_APP=main.py FLASK_ENV=development flask run

### Data Manipulation format:

> GET values: ==> [http://localhost:5000/values](http://localhost:5000/values) or [http://localhost:5000/values?keys=key1,key2](http://localhost:5000/values?keys=key1,key2)

> POST to: ==> [http://localhost:5000/values](http://localhost:5000/values) format is bellow:
```
    {
        "key1": 1234567890,
        "key2": "Just some string",
        "key3": ["Just", "some", "string"],
        "key4": [{"name": "unknown"}, ["a", "b", "c" ]],
        "key5": {"name": "anybody", "arrays": ["d","e"]}
    }
```

> EDIT (PATCH) to: ==> [http://localhost:5000/values](http://localhost:5000/values) format is bellow:
```
    {
        "key1": {"id": "5e05f7338199f29340af644e", "data": 12453}
    }
```