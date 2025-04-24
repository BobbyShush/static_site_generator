import unittest

from leafnode import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("BOLD AND BEAUTIFUL", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>BOLD AND BEAUTIFUL</b>")

    def test_italic(self):
        node = TextNode("You said Italian?", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>You said Italian?</i>")
    
    def test_code(self):
        node = TextNode("print('Hello world')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello world')</code>")

    def test_link(self):
        node = TextNode("anchorText", TextType.LINK, "www.iamatest.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="www.iamatest.com">anchorText</a>')

    def test_image(self):
        node = TextNode("altText", TextType.IMAGE, "/path/to/your/heart")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="/path/to/your/heart" alt="altText"></img>')
