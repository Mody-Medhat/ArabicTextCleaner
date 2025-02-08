# tests/test_remove_emojis.py

import unittest
from ArabicTextCleaner.remove_emojis import remove_emojis

class TestRemoveEmojis(unittest.TestCase):
    def test_remove_single_emoji(self):
        text = "مرحبا 😊"
        expected = "مرحبا "
        self.assertEqual(remove_emojis(text), expected)

    def test_remove_multiple_emojis(self):
        text = "😊 مرحبا 😊 كيف الحال؟ 😊"
        expected = " مرحبا  كيف الحال؟ "
        self.assertEqual(remove_emojis(text), expected)

    def test_no_emojis(self):
        text = "مرحبا كيف الحال؟"
        expected = text
        self.assertEqual(remove_emojis(text), expected)

if __name__ == '__main__':
    unittest.main()
