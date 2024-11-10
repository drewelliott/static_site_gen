#!/usr/bin/env python3
import unittest

from htmlnode import HTMLNode

# Need to test these conditions: 
#  - An HTMLNode without a tag will render as raw text
#  - An HTMLNode without a value will be assumed to have children
#  - An HTMLNode without children will be assumed to have a value
#  - An HTMLNode without props simply won't have any attributes

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        # not sure how to test this one yet
        pass

    def test_value(self):
        node = HTMLNode(tag='p', 
                value='The quick brown fox jumped over the lazy dog', 
                props={'href': 'https://www.google.com', 'target': '_blank'})
        expected_props = ' href=https://www.google.com target=_blank'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_repr(self):
        node = HTMLNode(tag='p', 
                value='The quick brown fox jumped over the lazy dog', 
                props={'href': 'https://www.google.com', 'target': '_blank'})
        expected_repr = "HTMLNode(p, The quick brown fox jumped over the lazy dog, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
        
