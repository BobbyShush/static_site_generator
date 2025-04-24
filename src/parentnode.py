from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")

    def to_html(self):
        props_html = self.props_to_html() if self.props else ""
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{props_html}>{html_string}</{self.tag}>"
