from textnode import TextType, TextNode
from from_dir_to_dir import copy_from_dir_to_dir

def main():
    node = TextNode("This is text", TextType.BOLD, "https://url.com")
    print(node)
    copy_from_dir_to_dir()

main()