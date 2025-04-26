import unittest

from md_to_htmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here\n"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```This is text that _should_ remain\nthe **same** even with inline stuff\n```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = """
    # Heading 1

    ## Heading 2

    ### Heading 3

    #### Heading 4

    ##### Heading 5

    ###### Heading 6
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>"
        )

    def test_quote_blocks(self):
        md = """>This is a quote
>With multiple lines

>This is another quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><blockquote>This is a quote With multiple lines</blockquote><blockquote>This is another quote</blockquote></div>"
        self.assertEqual(html, expected)
    
    def test_unordered_list(self):
        md = """- Item 1\n- Item 2\n- Item with **bold** text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item with <b>bold</b> text</li></ul></div>",
        )
    
    def test_ordered_list(self):
        md = """1. First item\n2. Second item\n3. Item with `code`"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Item with <code>code</code></li></ol></div>",
        )

    def test_edge_cases(self):
        #1 Empty Document
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
        "<div></div>"
        )
