import unittest
from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):

    def test_code(self):
        node = TextNode("This is a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode(text='This is a ', text_type=TextType.NORMAL, url=None), 
                TextNode(text='code block', text_type=TextType.CODE, url=None), 
                TextNode(text=' word', text_type=TextType.NORMAL, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_italic(self):
        node = TextNode("This is an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
                TextNode(text='This is an ', text_type=TextType.NORMAL, url=None), 
                TextNode(text='italic', text_type=TextType.ITALIC, url=None), 
                TextNode(text=' word', text_type=TextType.NORMAL, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_bold(self):
        node = TextNode("This is a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
                TextNode(text='This is a ', text_type=TextType.NORMAL, url=None), 
                TextNode(text='bold', text_type=TextType.BOLD, url=None), 
                TextNode(text=' word', text_type=TextType.NORMAL, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_bad_markdown(self):
        node = TextNode("This is a **bold word", TextType.NORMAL)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_texttype_not_normal(self):
        node = TextNode("This TextType is not NORMAL", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode(text='This TextType is not NORMAL', text_type=TextType.CODE, url=None)
        ]
        self.assertEqual(expected, new_nodes)
        