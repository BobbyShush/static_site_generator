from textnode import TextType, TextNode

def main():
    node = TextNode("This is text", TextType.BOLD, "https://url.com")
    print(node)

main()