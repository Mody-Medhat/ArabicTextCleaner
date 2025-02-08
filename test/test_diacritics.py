# tests/test_diacritics.py
import unittest
from ArabicTextCleaner.diacritics import remove_diacritics

class TestDiacritics(unittest.TestCase):
    def test_remove_diacritics(self):
        self.assertEqual(remove_diacritics("مُحَمَّدٌ"), "محمد")

if __name__ == '__main__':
    unittest.main()
