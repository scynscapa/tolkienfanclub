import unittest

from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(
            extract_title("# Hello"),
            "Hello"
        )

if __name__ == "__main__":
    unittest.main()