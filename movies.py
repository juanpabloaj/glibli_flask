def id_from_url(url):
    return url.split("/")[-1]


def films_ids_from_person(person):
    return [id_from_url(film) for film in person["films"]]


def movies_with_people(movies, people):
    with_people = []
    by_movie = {}

    for person in people:
        name = person["name"]
        ids = films_ids_from_person(person)

        for film_id in ids:
            if film_id not in by_movie.keys():
                by_movie[film_id] = [name]
            else:
                by_movie[film_id].append(name)

    for movie in movies:
        people = []

        movie_id = movie["id"]
        if movie_id in by_movie.keys():
            people = by_movie[movie_id]

        with_people.append({"title": movie["title"], "people": people})

    return with_people
