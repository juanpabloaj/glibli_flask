import pytest
import unittest

from app import app


class TestService(unittest.TestCase):
    def test_root(self):
        tester = app.test_client(self)

        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, b"hello flask")
