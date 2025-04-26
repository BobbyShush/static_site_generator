import unittest

from md_to_block import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        #1
        block = "I am a paragraph\nWith new lines\nAnd all that jazz"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #2
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        #1
        block = "# I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #2
        block = "## I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #3
        block = "### I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #4
        block = "#### I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #5
        block = "##### I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #6
        block = "###### I am a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        #7
        block = "####### I am NOT a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        #1
        block = "``` I am a block of code ```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        #2
        block = "```\n>A code block\n>with line breaks\n>that look like\n>a quote\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        #3
        block = "```\n- A code block\n- with line breaks\n- that look like\n- an unordered list\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        #4
        block = "````An extra tick won't hurt````"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        #5
        block = "```Not a code block``"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #6
        block = "```\n1. OK\n2. I'll do\n3. The ordered list\n4. Too\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        #7
        block = "``````"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_ul(self):
        #1
        block = "- Item A\n- Item B\n- Item C"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        #2
        block = "- Item A\n> Item B\n- Item C"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #3
        block = "* Item A\n* Item B\n* Item C"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #4
        block = "- Item A```\n- Item B```\n- Item C"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_ol(self):
        #1
        block = "1. Item A\n2. Item B\n3. Item C"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        #2
        block = "1. Item A\n3. Item B\n2. Item C"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #3
        block = "1. Item A\n2.Item B\n3. Item C"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        #4
        block = "1. Item A```\n2. Item B```\n3. Item C"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

