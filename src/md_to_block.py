from enum import Enum
import re

HEADING_PATTERN = re.compile(r'^#{1,6} ')
CODE_PATTERN = re.compile(r'^```.*```$', re.DOTALL)
QUOTE_PATTERN = re.compile(r'^>\s*.*(?:\n>\s*.*)*$', re.MULTILINE)
UNORDERED_LIST_PATTERN = re.compile(r'^- .*(\n- .*)*$')

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(filter(lambda x: x != "",map(lambda x: x.strip(), blocks)))

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()  # Remove '# ' and trim
    # If no h1 header is found, raise an exception
    raise Exception("No h1 header found in markdown")

def block_to_block_type(block):
    if HEADING_PATTERN.match(block):
        return BlockType.HEADING
    if CODE_PATTERN.match(block):
        return BlockType.CODE
    if QUOTE_PATTERN.match(block):
        return BlockType.QUOTE
    if UNORDERED_LIST_PATTERN.match(block):
        return BlockType.UNORDERED_LIST
    
    # For ordered lists, check each line individually
    lines = block.split('\n')
    is_ordered_list = True
    
    for i, line in enumerate(lines):
        # Check if line starts with (i+1) followed by ". "
        expected_prefix = f"{i+1}. "
        if not line.startswith(expected_prefix):
            is_ordered_list = False
            break
    
    if is_ordered_list and lines:  # Ensure there's at least one line
        return BlockType.ORDERED_LIST
    
    # If none of the above match, it's a paragraph
    return BlockType.PARAGRAPH
