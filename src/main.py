import sys

from textnode import TextType, TextNode
from from_dir_to_dir import copy_from_dir_to_dir, generate_page_recursive

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
    copy_from_dir_to_dir(to_dir="docs")
    generate_page_recursive("content", "template.html", "docs", basepath)

main()