import unittest
import pytest

from app import app


@pytest.mark.skip("to develop with mocks")
class TestService(unittest.TestCase):
    def test_root(self):
        tester = app.test_client(self)

        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, b"hello flask")
