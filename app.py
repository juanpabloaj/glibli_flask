from flask import Flask

app = Flask(__name__)

GLIBLI_URL = "https://ghibliapi.herokuapp.com"


@app.route("/")
def root():
    return "hello flask"
