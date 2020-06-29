from flask import Flask, render_template

app = Flask(__name__)

GLIBLI_URL = "https://ghibliapi.herokuapp.com"


@app.route("/")
def root():
    return "Hello Glibli's fans"


@app.route("/movies")
def movies():
    movies = [
        {
            "title": "My Neighbor Totoro",
            "people": ["Mei Kusakabe", "Satsuki Kusakabe", "Tatsuo Kusakabe"],
        }
    ]
    return render_template("movies.html", movies=movies)
