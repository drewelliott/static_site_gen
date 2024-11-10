#!/usr/bin/env python3
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_initialization(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_children(self):
        node = HTMLNode(
                tag='ul',
                children='li'
        )
        self.assertEqual(node.children, "li")

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)
        
    def test_empty_props(self):
        node = HTMLNode(tag='h1', value="Header1") 
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode(
                tag='a',
                props={"href": "https://www.yahoo.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.yahoo.com"')

    def test_repr(self):
        node = HTMLNode(
                tag='p', 
                value='The quick...', 
                props={'target': '_blank'}
        )
        expected_repr = "HTMLNode(tag='p', value='The quick...', children=None, props={'target': '_blank'})"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
        
