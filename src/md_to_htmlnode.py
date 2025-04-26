from md_to_block import BlockType, markdown_to_blocks, block_to_block_type
from textnode import text_to_textnodes, TextType, TextNode
from parentnode import ParentNode
from leafnode import LeafNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    result = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case (BlockType.PARAGRAPH):
                block_content = block.replace("\n", " ")
                children = text_to_children(block_content)
                node = ParentNode("p", children)
                result.append(node)
            case (BlockType.HEADING):
                level = count_hashes(block)
                content = block[level:].strip().replace("\n", " ")
                children = text_to_children(content)
                node = ParentNode(f"h{level}", children)
                result.append(node)
            case (BlockType.CODE):
                content = block[3:-3]
                text_node = text_node_to_html_node(TextNode(content, TextType.TEXT))
                code_node =  ParentNode("code",  [text_node])
                node = ParentNode("pre", [code_node])
                result.append(node)
            case (BlockType.QUOTE):
                result.append(process_quote_block(block))
            case (BlockType.UNORDERED_LIST):
                lines = block.split("\n")
                children = []
                for line in lines:
                    grandchildren = text_to_children(line[2:].strip())
                    list_item = ParentNode("li", grandchildren)
                    children.append(list_item)
                node = ParentNode("ul", children)
                result.append(node)
            case (BlockType.ORDERED_LIST):
                lines = block.split("\n")
                children = []
                for line in lines:
                    grandchildren = text_to_children(line[3:].strip())
                    list_item = ParentNode("li", grandchildren)
                    children.append(list_item)
                node = ParentNode("ol", children)
                result.append(node)
            case _:
                raise Exception("Invalid BlockType")
    return ParentNode("div", result)

def text_to_children(markdown):
    text_nodes = text_to_textnodes(markdown)
    return list(map(text_node_to_html_node, text_nodes))

def count_hashes(heading_block):
    level = 0
    for char in heading_block:
        if char == '#':
            level += 1
        else:
            break
    return level

def process_quote_block(block):
    lines = block.strip().split("\n")
    content = ""
    for line in lines:
        # Remove the '>' character and preserve spaces
        content += line.strip()[1:].lstrip() + " "  # Note the space here
    
    # Remove trailing space and create node
    return ParentNode("blockquote", text_to_children(content.strip()))