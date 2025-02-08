# tests/test_remove_links.py

import unittest
from ArabicTextCleaner.remove_links import remove_links

class TestRemoveLinks(unittest.TestCase):
    def test_remove_http_link(self):
        text = "زور http://example.com للمزيد"
        expected = "زور للمزيد"
        self.assertEqual(remove_links(text), expected)

if __name__ == '__main__':
    unittest.main()
