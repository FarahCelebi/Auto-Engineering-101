import unittest
from vowels import count_vowels


class TestVowelCounter(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_single_vowel(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("A"), 1)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_mixed_characters(self):
        self.assertEqual(count_vowels("Hello World!"), 3)
        self.assertEqual(count_vowels("PyCharm"), 1)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aEiOu"), 5)


if __name__ == "__main__":
    unittest.main()