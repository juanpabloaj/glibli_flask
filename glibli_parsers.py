def info_from_films(films):
    info = []

    for film in films:
        info.append({"name": film["name"], "id": film["id"]})

    return info
