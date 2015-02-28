import unittest
import flask
import photolog
from photolog import app


class TestIndexView(unittest.TestCase):
    def test_it_runs(self):
        with app.test_request_context("/"):
            result = photolog.index()
            self.assertIn("bem-vindo", result.lower())

if __name__ == "__main__":
    unittest.main()