import unittest
from palindrome import is_palindrome


class TestPalindromeChecker(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_mixed_characters(self):
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_with_special_characters(self):
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertTrue(is_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_palindrome("Able was I, I saw Elba"))


if __name__ == "__main__":
    unittest.main()