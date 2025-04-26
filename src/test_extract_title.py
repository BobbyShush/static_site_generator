import unittest

from md_to_block import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract(self):
        #1
        md = "# I am a title\n\n"
        self.assertEqual(extract_title(md), "I am a title")