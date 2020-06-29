import unittest
import pytest

from app import app


class TestService(unittest.TestCase):
    def test_root(self):
        tester = app.test_client(self)

        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, b"Hello Glibli's fans!!")


@pytest.mark.skip("test with mocks")
class TestMoviesRoute(unittest.TestCase):
    def test_movies(self):
        pass
