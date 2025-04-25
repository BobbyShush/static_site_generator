import unittest

from textnode import TextNode, TextType, split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_odd_delimiters(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([TextNode("foo*bar*baz*qux", TextType.TEXT)], "*", TextType.BOLD)
        self.assertEqual(str(context.exception), "Invalid Markdown syntax")

    def test_unmatched_delimiters(self):
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([TextNode("foo*bar-baz", TextType.TEXT)], "*", TextType.ITALIC)
        self.assertEqual(str(context.exception), "Invalid Markdown syntax")

    def test_no_delimiter(self):
        nodes = [TextNode("foo bar baz", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("foo bar baz", TextType.TEXT)])

    def test_text_type(self):
        nodes = [TextNode("foo*bar*baz*qux*", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("foo", TextType.TEXT),
            TextNode("bar", TextType.TEXT),
            TextNode("baz", TextType.TEXT),
            TextNode("qux", TextType.TEXT)
            ])

    def test_normal_cases(self):
        nodes = [TextNode("foo*bar*baz*qux*", TextType.TEXT), 
        TextNode("foo**bar*baz**qux*", TextType.TEXT),
        TextNode("Supposed*to*be*code*", TextType.CODE)
        ]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        self.assertEqual(new_nodes,[
            TextNode("foo", TextType.TEXT),
            TextNode("bar", TextType.BOLD),
            TextNode("baz", TextType.TEXT),
            TextNode("qux", TextType.BOLD),
            TextNode("foo", TextType.TEXT),
            TextNode("bar", TextType.TEXT),
            TextNode("baz", TextType.BOLD),
            TextNode("qux", TextType.BOLD),
            TextNode("Supposed*to*be*code*", TextType.CODE)
        ])
    