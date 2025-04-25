import unittest

from textnode import TextNode, TextType, split_nodes_image, split_nodes_link

class TestSplitImageLink(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](www.iamatest.com) and another [second link](www.iamasecondtest.com) and yet another ![psych](www.iamanimage.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "www.iamatest.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "www.iamasecondtest.com"),
                TextNode(" and yet another ![psych](www.iamanimage.com)", TextType.TEXT)
            ],
            new_nodes
        )