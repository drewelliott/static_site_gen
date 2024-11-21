import unittest
from src.texttotextnodes import text_to_textnodes
from src.textnode import TextNode, TextType


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
        text = "![this](image.jpg) is an image"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="this", text_type=TextType.IMAGE, url="image.jpg"),
                TextNode(text=" is an image", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_link(self):
        text = "[this](https://yahoo.com) is a link"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="this", text_type=TextType.LINK, url="https://yahoo.com"),
                TextNode(text=" is a link", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_all_bold(self):
        text = "**Bold words are really cool.**"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None),
                TextNode(text="Bold words are really cool.", text_type=TextType.BOLD, url=None),
                TextNode(text="", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_all_italic(self):
        text = "*Italic words are really cool.*"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None),
                TextNode(text="Italic words are really cool.", text_type=TextType.ITALIC, url=None),
                TextNode(text="", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_all_code(self):
        text = "`Code blocks are really cool.`"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None),
                TextNode(text="Code blocks are really cool.", text_type=TextType.CODE, url=None),
                TextNode(text="", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_only_image(self):
        text = "![only image](image.jpg)"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="only image", text_type=TextType.IMAGE, url="image.jpg")
                ]
        self.assertEqual(expected, new_nodes)


    def test_three_bold(self):
        text = "**Bold** words **are** really **cool**."
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None),
                TextNode(text="Bold", text_type=TextType.BOLD, url=None),
                TextNode(text=" words ", text_type=TextType.TEXT, url=None),
                TextNode(text="are", text_type=TextType.BOLD, url=None),
                TextNode(text=" really ", text_type=TextType.TEXT, url=None),
                TextNode(text="cool", text_type=TextType.BOLD, url=None),
                TextNode(text=".", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)

        
    def test_three_italic(self):
        text = "**Italic** words **are** really **cool**."
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="", text_type=TextType.TEXT, url=None),
                TextNode(text="Italic", text_type=TextType.BOLD, url=None),
                TextNode(text=" words ", text_type=TextType.TEXT, url=None),
                TextNode(text="are", text_type=TextType.BOLD, url=None),
                TextNode(text=" really ", text_type=TextType.TEXT, url=None),
                TextNode(text="cool", text_type=TextType.BOLD, url=None),
                TextNode(text=".", text_type=TextType.TEXT, url=None)
                ]
        self.assertEqual(expected, new_nodes)


    def test_all_different(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        expected = [
                TextNode(text="This is ", text_type=TextType.TEXT, url=None),
                TextNode(text="text", text_type=TextType.BOLD, url=None),
                TextNode(text=" with an ", text_type=TextType.TEXT, url=None),
                TextNode(text="italic", text_type=TextType.ITALIC, url=None),
                TextNode(text=" word and a ", text_type=TextType.TEXT, url=None),
                TextNode(text="code block", text_type=TextType.CODE, url=None),
                TextNode(text=" and an ", text_type=TextType.TEXT, url=None),
                TextNode(text="obi wan image", text_type=TextType.IMAGE, url="https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(text=" and a ", text_type=TextType.TEXT, url=None),
                TextNode(text="link", text_type=TextType.LINK, url="https://boot.dev")         
                ]
