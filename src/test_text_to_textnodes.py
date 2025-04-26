import unittest

from textnode import TextNode, TextType, text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        # Test 1: Basic test with all markdown elements
        text = "This is **bold** and _italic_ with `code` and an ![image](image.jpg) and a [link](https://example.com)"
        nodes = text_to_textnodes(text)

        # Add this line to print the actual nodes for debugging
        # print(f"Number of nodes: {len(nodes)}")
        # for i, node in enumerate(nodes):
        #    print(f"Node {i}: {node.text} - {node.text_type} - {getattr(node, 'url', 'No URL')}")
        
        assert len(nodes) == 10
        assert nodes[0].text == "This is "
        assert nodes[0].text_type == TextType.TEXT
        
        assert nodes[1].text == "bold"
        assert nodes[1].text_type == TextType.BOLD
        
        assert nodes[2].text == " and "
        assert nodes[2].text_type == TextType.TEXT
        
        assert nodes[3].text == "italic"
        assert nodes[3].text_type == TextType.ITALIC
        
        assert nodes[4].text == " with "
        assert nodes[4].text_type == TextType.TEXT
        
        assert nodes[5].text == "code"
        assert nodes[5].text_type == TextType.CODE
        
        assert nodes[6].text == " and an "
        assert nodes[6].text_type == TextType.TEXT
        
        assert nodes[7].text == "image"
        assert nodes[7].text_type == TextType.IMAGE
        assert nodes[7].url == "image.jpg"
        
        assert nodes[8].text == " and a "
        assert nodes[8].text_type == TextType.TEXT
        
        assert nodes[9].text == "link"
        assert nodes[9].text_type == TextType.LINK
        assert nodes[9].url == "https://example.com"

        # Test 2: Plain text with no markdown
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        
        assert len(nodes) == 1
        assert nodes[0].text == "Just plain text"
        assert nodes[0].text_type == TextType.TEXT
        
        # Test 3: Test nested markdown (though not required by the spec)
        text = "**Bold with _italic_ inside**"
        nodes = text_to_textnodes(text)

        assert len(nodes) == 1
        assert nodes[0].text == "Bold with _italic_ inside"
        assert nodes[0].text_type == TextType.BOLD
        
        # Test 4: Test multiple instances of the same markdown
        text = "**Bold** and **more bold**"
        nodes = text_to_textnodes(text)

        assert len(nodes) == 3
        assert nodes[0].text == "Bold"
        assert nodes[0].text_type == TextType.BOLD
        assert nodes[1].text == " and "
        assert nodes[1].text_type == TextType.TEXT
        assert nodes[2].text == "more bold"
        assert nodes[2].text_type == TextType.BOLD