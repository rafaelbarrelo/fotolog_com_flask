import unittest
import photolog


class MyTests(unittest.TestCase):
    def test_check_if_running(self):
        result = photolog.index()
        self.assertIn("bem-vindo", result.lower())

    def test_if_result_is_html(self):
        result = photolog.index()
        first_line = result.split("\n")[0]
        self.assertIn("html", first_line.lower())


if __name__ == "__main__":
    unittest.main()
