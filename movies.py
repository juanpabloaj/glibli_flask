def movies_with_people(movies, people):
    with_people = []

    for movie in movies:
        with_people.append({"title": movie["title"], "people": []})

    return with_people