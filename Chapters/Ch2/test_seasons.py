import unittest
from season_handler import get_season_response

class TestSeasonHandler(unittest.TestCase):

    def test_winter(self):
        self.assertEqual(get_season_response("winter"), "snow")

    def test_spring(self):
        self.assertEqual(get_season_response("spring"), "flowers")

    def test_summer(self):
        self.assertEqual(get_season_response("summer"), "beach")

    def test_fall(self):
        self.assertEqual(get_season_response("fall"), "leaves")

    def test_autumn(self):
        self.assertEqual(get_season_response("autumn"), "leaves")

    def test_unknown_season(self):
        self.assertEqual(get_season_response("monsoon"), "I don't know that season")
        self.assertEqual(get_season_response(""), "I don't know that season")

if __name__ == "__main__":
    unittest.main()