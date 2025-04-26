from textnode import TextType, TextNode
from from_dir_to_dir import copy_from_dir_to_dir, generate_page_recursive

def main():
    copy_from_dir_to_dir()
    generate_page_recursive("content", "template.html", "public")

main()