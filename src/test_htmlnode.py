import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="p", value="I am a paragraph", props={"href": "https://www.google.com"})
        print(node)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        print(node.props_to_html())
    
    def test_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        child3 = HTMLNode()
        node = HTMLNode(children=[child1, child2, child3])
        print(node)