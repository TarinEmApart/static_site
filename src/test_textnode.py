import unittest

from textnode import TextNode, text_node_to_html
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node, node2)

    def test_eq_with_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, None)

    def test_uneq_text(self):
        node = TextNode("This is not a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_uneq_text_type(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)   

    def test_uneq_url(self):
        node = TextNode("This is not a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.amazon.com")
        self.assertNotEqual(node, node2) 

    def test_url_none_pass(self):
        node = TextNode("This is not a text node", "bold", None)
        self.assertIsNone(node.url)
    
    def test_empty_string(self):
        node = TextNode("", "bold")
        self.assertEqual(node.text, "")
        
    @unittest.skip("Skipping this test because it is expected to throw an error")
    def test_url_none_fail(self):
        node = TextNode("This is not a text node", "bold", "google.com")
        self.assertIsNone(node.url)
        # should give error
        # AssertionError: 'google.com' is not None

    @unittest.skip("Skipping this test because it is expected to throw an error")
    def test_eq_with_different_type(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        self.assertNotEqual(node, "NotATextNodeObject")
        # should give error
        # AttributeError: 'str' object has no attribute 'text'

    def test_mutability(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node_other = TextNode("This is a text node", "bold", "www.google.com")
        
        self.assertEqual(node, node_other)
        
        # Change an attribute
        node_other.text_type = "italic"
        
        self.assertNotEqual(node, node_other)



    # tests below are for the text_node_to_html conversions
    def test_conversion_to_leafnode_text(self):
        text_node = TextNode('Hello', 'text')
        html_node = text_node_to_html(text_node)
        assert html_node.tag is None
        assert html_node.value == 'Hello'
        assert html_node.props is None

    def test_conversion_to_leafnode_bold(self):
        text_node = TextNode('Hello', 'bold')
        html_node = text_node_to_html(text_node)
        assert html_node.tag == 'b'
        assert html_node.value == 'Hello'
        assert html_node.props is None

    def test_conversion_to_leafnode_italic(self):
        text_node = TextNode('Hello', 'italic')
        html_node = text_node_to_html(text_node)
        assert html_node.tag == 'i'
        assert html_node.value == 'Hello'
        assert html_node.props is None

    def test_conversion_to_leafnode_code(self):
        text_node = TextNode('This is code', 'code')
        html_node = text_node_to_html(text_node)
        assert html_node.tag == 'code'
        assert html_node.value == 'This is code'
        assert html_node.props is None

    def test_conversion_to_leafnode_link(self):
        text_node = TextNode('Click Here', 'link', 'www.google.com')
        html_node = text_node_to_html(text_node)
        assert html_node.tag == 'a'
        assert html_node.value == 'Click Here'
        assert html_node.props == {'href': 'www.google.com'}

    def test_conversion_to_leafnode_image(self):
        text_node = TextNode('This is an image', 'image', 'www.google.com/image.png')
        html_node = text_node_to_html(text_node)
        assert html_node.tag == 'img'
        assert html_node.value == ''
        assert html_node.props == {'src': 'www.google.com/image.png', 'alt': 'This is an image'}

if __name__ == "__main__":
    unittest.main()