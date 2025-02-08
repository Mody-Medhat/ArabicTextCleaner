# tests/test_punctuation.py
import unittest
from ArabicTextCleaner.punctuation import remove_punctuation

class TestPunctuation(unittest.TestCase):
    def test_remove_punctuation(self):
        input_text = "مرحبا، كيف حالك؟"
        expected = "مرحبا كيف حالك"
        self.assertEqual(remove_punctuation(input_text), expected)

if __name__ == '__main__':
    unittest.main()
