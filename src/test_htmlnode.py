import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()