import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):

    def test_props_empty(self):
        node = HTMLNode()

        self.assertEqual("HTMLNode(None, None, None, None)", node.__str__())

    def test_not_empty(self):
        node = HTMLNode("a", "b", [HTMLNode()], {"href": "https://google.com"})

        self.assertEqual(" href=\"https://google.com\"", node.props_to_html())

    def test_no_children(self):
        node = HTMLNode("a", "b", None, {"href": "https://google.com", "target": "test"})

        self.assertEqual(" href=\"https://google.com\" target=\"test\"", node.props_to_html())