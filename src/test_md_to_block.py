import unittest

from md_to_block import markdown_to_blocks

class TestMarkdowndToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        #1 - Normal test
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        #2 - With whitespace and empty blocks
        md = """
This is **bolded** paragraph



               WHITE SPACE WAS HERE! This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line BUT WITH WHITE SPACE AT THE END                      

- This is a list
- with items AND WHITE SPACE AS WELL!!!!         
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "WHITE SPACE WAS HERE! This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line BUT WITH WHITE SPACE AT THE END",
                "- This is a list\n- with items AND WHITE SPACE AS WELL!!!!",
            ],
        )

