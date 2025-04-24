import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "I am content")
        self.assertEqual(node.to_html(), "I am content")

    def test_leat_to_html_props(self):
        node = LeafNode("a", "I am content", {"href": "www.iamatest.com"})
        self.assertEqual(node.to_html(), '<a href="www.iamatest.com">I am content</a>')

    def test_leaf_node_requires_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Content in a div")
        self.assertEqual(node.to_html(), "<div>Content in a div</div>")

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("img", "Alt text", {"src": "image.jpg", "alt": "An image", "width": "100"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="An image" width="100">Alt text</img>')
    
    def test_leaf_to_html_special_chars(self):
        node = LeafNode("p", "Text with <special> & \"characters\"")
        self.assertEqual(node.to_html(), "<p>Text with <special> & \"characters\"</p>")