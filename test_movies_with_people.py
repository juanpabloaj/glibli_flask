import unittest
import pytest
from movies import movies_with_people, id_from_url


class TestIdFromUrl(unittest.TestCase):
    def test_get_id(self):
        url = (
            "https://ghibliapi.herokuapp.com/films/"
            "758bf02e-3122-46e0-884e-67cf83df1786"
        )

        expected = "758bf02e-3122-46e0-884e-67cf83df1786"

        assert id_from_url(url) == expected


class TestMoviesWithPeople(unittest.TestCase):
    def test_movies_and_people_empty(self):
        movies = []
        people = []
        with_people = movies_with_people(movies, people)

        assert with_people == []

    def test_movie_with_empty_people(self):
        movies = [
            {"title": "Castle in the Sky", "id": "a0"},
            {"title": "Grave of the Fireflies", "id": "b1"},
        ]

        expected = [
            {"title": "Castle in the Sky", "people": []},
            {"title": "Grave of the Fireflies", "people": []},
        ]

        with_people = movies_with_people(movies, [])

        assert with_people == expected

    @pytest.mark.skip("to develop")
    def test_with_movies_and_people(self):
        people = [
            {
                "name": "Ashitaka",
                "films": [
                    "http://ghi.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
                ],
            },
            {
                "name": "San",
                "films": [
                    "http://ghi.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
                ],
            },
            {
                "name": "Sosuke",
                "films": [
                    "http://ghi.com/films/758bf02e-3122-46e0-884e-67cf83df1786"
                ],
            },
        ]

        movies = [
            {
                "id": "0440483e-ca0e-4120-8c50-4c8cd9b965d6",
                "title": "Princess Mononoke",
            },
            {"id": "758bf02e-3122-46e0-884e-67cf83df1786", "title": "Ponyo"},
        ]

        expected = [
            {"title": "Princess Mononoke", "people": ["Ashitaka", "San"]},
            {"title": "Ponyo", "people": ["Sosuke"]},
        ]

        with_people = movies_with_people(movies, people)

        assert with_people == expected
