import unittest
from glibli_parsers import info_from_films


class TestNameFromFilms(unittest.TestCase):
    def test_empty_list(self):
        response = []
        info = info_from_films(response)

        self.assertEqual(info, [])

    def test_name_and_id_from_film(self):
        response = [{"id": "abc", "name": "Ponyo", "producer": "T Suzuki"}]

        expected = [{"id": "abc", "name": "Ponyo"}]

        info = info_from_films(response)
        self.assertEqual(info, expected)
