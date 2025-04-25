import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="p", value="I am a paragraph", props={"href": "https://www.google.com"})
        self.assertEqual(f"{node}", "HTMLNode object.\n* Tag=p\n* value=I am a paragraph\n* children=None\n* props={'href': 'https://www.google.com'}")

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        child3 = HTMLNode()
        node = HTMLNode(children=[child1, child2, child3])
        self.assertEqual(f"{node}", "HTMLNode object.\n* Tag=None\n* value=None\n* children=[HTMLNode object.\n* Tag=None\n* value=None\n* children=None\n* props=None, HTMLNode object.\n* Tag=None\n* value=None\n* children=None\n* props=None, HTMLNode object.\n* Tag=None\n* value=None\n* children=None\n* props=None]\n* props=None")