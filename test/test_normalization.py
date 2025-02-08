import unittest
from ArabicTextCleaner.normalization import normalize_characters

class TestNormalization(unittest.TestCase):
    def test_normalize_alef(self):
        self.assertEqual(normalize_characters("أحمد"), "احمد")

if __name__ == '__main__':
    unittest.main()
