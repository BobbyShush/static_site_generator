from htmlnode import HTMLNode
from textnode import TextNode, TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
        if value is None:
            raise ValueError("LeafNode must have a value")
        
    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
            
        props_html = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case (TextType.IMAGE):
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise TypeError(f"Invalid text type: {text_node.text_type}")