import unittest
from texttotextnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
   
    def test_bold(self):
        text = "**This** word is bold"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None), 
                TextNode(text="This", text_type=TextType.BOLD, url=None), 
                TextNode(text=" word is bold", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_italic(self):
        text = "*This* word is italic"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None), 
                TextNode(text="This", text_type=TextType.ITALIC, url=None), 
                TextNode(text=" word is italic", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_code(self):
        text = "`This` word is code"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None), 
                TextNode(text="This", text_type=TextType.CODE, url=None), 
                TextNode(text=" word is code", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_image(self):
        text = "`This` word is code"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None), 
                TextNode(text="This", text_type=TextType.CODE, url=None), 
                TextNode(text=" word is code", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)

