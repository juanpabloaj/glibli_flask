from flask import Flask, render_template
import requests
from movies import movies_with_people
from cachetools import cached, TTLCache
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

GLIBLI_URL = "https://ghibliapi.herokuapp.com"


@cached(cache=TTLCache(maxsize=1024, ttl=60))
def request_data(url):
    app.logger.info("requesting %s", url)
    return requests.get(url).json()


@app.route("/")
def root():
    return "Hello Glibli's fans"


@app.route("/movies")
def movies():

    movies_url = GLIBLI_URL + "/films"
    people_url = GLIBLI_URL + "/people"

    movies = request_data(movies_url)
    people = request_data(people_url)

    with_people = movies_with_people(movies, people)

    return render_template("movies.html", movies=with_people)
