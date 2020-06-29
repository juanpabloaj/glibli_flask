from flask import Flask, render_template
import requests
from movies import movies_with_people

app = Flask(__name__)

GLIBLI_URL = "https://ghibliapi.herokuapp.com"


@app.route("/")
def root():
    return "Hello Glibli's fans"


@app.route("/movies")
def movies():

    movies_url = GLIBLI_URL + "/films"
    people_url = GLIBLI_URL + "/people"

    movies = requests.get(movies_url).json()
    people = requests.get(people_url).json()

    with_people = movies_with_people(movies, people)

    return render_template("movies.html", movies=with_people)
