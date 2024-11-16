import unittest
from textnode import TextNode, TextType
from split import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):

    def test_code(self):
        node = TextNode("This is a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode(text='This is a ', text_type=TextType.TEXT, url=None), 
                TextNode(text='code block', text_type=TextType.CODE, url=None), 
                TextNode(text=' word', text_type=TextType.TEXT, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_italic(self):
        node = TextNode("This is an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
                TextNode(text='This is an ', text_type=TextType.TEXT, url=None), 
                TextNode(text='italic', text_type=TextType.ITALIC, url=None), 
                TextNode(text=' word', text_type=TextType.TEXT, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_bold(self):
        node = TextNode("This is a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
                TextNode(text='This is a ', text_type=TextType.TEXT, url=None), 
                TextNode(text='bold', text_type=TextType.BOLD, url=None), 
                TextNode(text=' word', text_type=TextType.TEXT, url=None)
        ]
        self.assertEqual(expected, new_nodes)

    def test_bad_markdown(self):
        node = TextNode("This is a **bold word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_texttype_not_normal(self):
        node = TextNode("This TextType is not TEXT", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
                TextNode(text='This TextType is not TEXT', text_type=TextType.CODE, url=None)
        ]
        self.assertEqual(expected, new_nodes)
        
