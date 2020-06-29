
Usage

    pip install -r requirements.txt
    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=8000

Run tests

    pytest

Or

    ptw

Run code formatter and flake8

    black -l 79 . && flake8
