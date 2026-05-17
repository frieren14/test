import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://test.com", "target": "blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://test.com\" target=\"blank\">Hello, world!</a>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Hello, world!", {"href": "https://test.com", "target": "blank"})
        self.assertEqual(node.to_html(), "<span href=\"https://test.com\" target=\"blank\">Hello, world!</span>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!", {"href": "https://test.com", "target": "blank"})
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode(None, None, {"href": "https://test.com", "target": "blank"})
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()