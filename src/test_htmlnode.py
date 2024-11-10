#!/usr/bin/env python3
import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_leafnode_initialization(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph of text.")

    def test_leafnode_props_to_html(self):
        node = LeafNode("a", "Yahoo!", {"href": "https://www.yahoo.com"})
        expected = '<a href="https://www.yahoo.com">Yahoo!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_to_html(self):
        node = LeafNode("b", "You are rather bold!")
        expected = '<b>You are rather bold!</b>'
        self.assertEqual(node.to_html(), expected)



if __name__ == "__main__":
    unittest.main()
        
