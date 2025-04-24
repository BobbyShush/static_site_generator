import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test2(self):
        node = TextNode("Not the same", TextType.NORMAL, "www.iamatest.com")
        node2 = TextNode("Notte ze thame", TextType.NORMAL, "www.iamatest.com")
        self.assertNotEqual(node, node2)

    def test3(self):
        node = TextNode("Not the same", TextType.NORMAL)
        node2 = TextNode("Not the same", TextType.NORMAL, "www.iamatest.com")
        self.assertNotEqual(node, node2)

    def test4(self):
        node = TextNode("Not the same", TextType.LINK, "www.iamatest.com")
        node2 = TextNode("Not the same", TextType.NORMAL, "www.iamatest.com")
        self.assertNotEqual(node, node2)

    def test5(self):
        node = TextNode("The same", TextType.CODE, "www.iamatest.com")
        node2 = TextNode("The same", TextType.CODE, "www.iamatest.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()