from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # this if statement is for explicit type-checking.
        # it ensures comparisons with 'None' or any other
        # type won't throw an exception
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text 
                and self.text_type == other.text_type
                and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html(text_node):
    values = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in values:
        raise Exception("Invalid text type.")
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})