from enum import Enum
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text 
        and self.text_type == other.text_type 
        and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown syntax")

        split_text = node.text.split(delimiter)
        for i, part in enumerate(split_text):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        found_images = extract_markdown_images(original_text)
        if node.text_type != TextType.TEXT or not found_images:
            new_nodes.append(node)
            continue

        image_alt = found_images[0][0]
        image_link = found_images[0][1]
        sections = original_text.split(f"![{image_alt}]({image_link})", 1)
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
        if sections[1]:
            new_nodes.extend(split_nodes_image([TextNode(sections[1], TextType.TEXT)]))
    return new_nodes        


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        found_links = extract_markdown_links(original_text)
        if node.text_type != TextType.TEXT or not found_links:
            new_nodes.append(node)
            continue

        link_text = found_links[0][0]
        link_url = found_links[0][1]
        sections = original_text.split(f"[{link_text}]({link_url})", 1)
        if sections[0]:
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        if sections[1]:
            new_nodes.extend(split_nodes_link([TextNode(sections[1], TextType.TEXT)]))
    return new_nodes     


def text_to_textnodes(text):
    parsed_bold = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    parsed_italic = split_nodes_delimiter(parsed_bold, "_", TextType.ITALIC)
    parsed_code = split_nodes_delimiter(parsed_italic, "`", TextType.CODE)
    parsed_images = split_nodes_image(parsed_code)
    parsed_links = split_nodes_link(parsed_images)
    return parsed_links