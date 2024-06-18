import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        output = " href=\"https://www.google.com\" target=\"_blank\""
        result = node.props_to_html()
        self.assertEqual(result, output)
    
    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        output = " href=\"https://www.google.com\""
        result = node.props_to_html()
        self.assertEqual(result, output)
    
    def test_props_to_html_empty_props(self):
        node = HTMLNode(props={})
        output = ""
        result = node.props_to_html()
        self.assertEqual(result, output)
    
    def test_props_to_html_special_characters(self):
        node = HTMLNode(props={"data-special": "value&special"})
        output = " data-special=\"value&special\""
        result = node.props_to_html()
        self.assertEqual(result, output)
    
    def test_props_to_html_no_props_provided(self):
        node = HTMLNode()
        self.assertEqual(node.props, None)

    class TestLeafNode(unittest.TestCase):
        def test_to_html_paragraph(self):
            leaf = LeafNode("p", "This is a paragraph of text.")
            self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

        def test_to_html_link(self):
            leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
            self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

        def test_to_html_no_value_raises_error(self):
            with self.assertRaises(ValueError):
                leaf = LeafNode("p")
                leaf.to_html()

        def test_to_html_no_tag_returns_value(self):
            leaf = LeafNode(value="Just a string, no tag")
            self.assertEqual(leaf.to_html(), "Just a string, no tag")


if __name__ == "__main__":
    unittest.main()