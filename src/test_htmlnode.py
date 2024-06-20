import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        result = '<a href="https://www.google.com">Click me!</a>'
        output = leaf.to_html()
        self.assertEqual(result, output)

    def test_to_html_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode("p")
            leaf.to_html()

    def test_to_html_no_tag_returns_value(self):
        leaf = LeafNode(value="Just a string, no tag")
        self.assertEqual(leaf.to_html(), "Just a string, no tag")

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        result = parent.to_html()
        self.assertEqual(result, output)
    
    def test_nested_parent_nodes(self):
        parent = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "First paragraph."),
                        LeafNode("b", "Bold text in first paragraph."),
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "Italic text in second paragraph."),
                        LeafNode(None, "Second paragraph."),
                    ]
                ),
            ]
        )
        output = ("<div><p>First paragraph.<b>Bold text in first paragraph.</b></p>"
                "<p><i>Italic text in second paragraph.</i>Second paragraph.</p></div>")
        result = parent.to_html()
        self.assertEqual(result, output)

    def test_nested_parent_node_with_props(self):
        parent = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Click me!", {"href": "https://www.google.com"} ),
                        LeafNode("b", "Bold text in first paragraph."),
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                        LeafNode(None, "Second paragraph."),
                    ]
                ),
            ]
        )
        output = ("<div><p><a href=\"https://www.google.com\">Click me!</a><b>Bold text in first paragraph.</b></p>"
                "<p><a href=\"https://www.google.com\">Click me!</a>Second paragraph.</p></div>")
        result = parent.to_html()
        self.assertEqual(result, output)

    def test_for_none_tag_or_missing_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(
                "div",
                [
                    ParentNode(
                        "p",
                        [
                            LeafNode(None, None, None ),
                        ]
                    ),
                ]
            )
            parent.to_html()

    def test_mixing_leafnode_and_parentnode_children(self):
        parent = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Click me!", {"href": "https://www.google.com"} ),
                        LeafNode("b", "Bold text in first paragraph."),
                    ]
                ),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),         
            ],
        )
        output = ("<div><p><a href=\"https://www.google.com\">Click me!</a><b>Bold text in first paragraph.</b></p>"
                "<a href=\"https://www.google.com\">Click me!</a></div>")
        result = parent.to_html()
        self.assertEqual(result, output)


    def test_empty_props(self):
        parent = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Click me!", {None: None} ),
                        LeafNode("b", "Bold text in first paragraph."),
                    ]
                ),
            ],
        )
        output = ("<div><p><a>Click me!</a><b>Bold text in first paragraph.</b></p></div>")
        result = parent.to_html()
        self.assertEqual(result, output)

if __name__ == "__main__":
    unittest.main()