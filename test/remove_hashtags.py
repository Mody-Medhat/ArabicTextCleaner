# tests/test_remove_hashtags.py

import unittest
from ArabicTextCleaner.remove_hashtags import remove_hashtags

class TestRemoveHashtags(unittest.TestCase):
    def test_remove_single_hashtag(self):
        text = "هذا مثال على #تنظيف_النص"
        expected = "هذا مثال على "
        self.assertEqual(remove_hashtags(text), expected)

    def test_remove_multiple_hashtags(self):
        text = "#مرحبا هذا #مثال على #تنظيف_النص"
        expected = " هذا  على "
        self.assertEqual(remove_hashtags(text), expected)

    def test_no_hashtags(self):
        text = "هذا مثال على تنظيف النص"
        expected = text
        self.assertEqual(remove_hashtags(text), expected)

if __name__ == '__main__':
    unittest.main()
