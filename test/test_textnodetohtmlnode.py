import unittest
from src.textnode import TextNode, TextType
from src.textnodetohtmlnode import text_node_to_html_node


class TestTransform(unittest.TestCase):

    def test_text_conversion(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertEqual(html_node.props, None)

    def test_bold_conversion(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)

    def test_italic_conversion(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)

    def test_code_conversion(self):
        text_node = TextNode("greeting = 'Hello, world!'\nprint(greeting)", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "greeting = 'Hello, world!'\nprint(greeting)")
        self.assertEqual(html_node.props, None)

    def test_link_conversion(self):
        text_node = TextNode("link test", TextType.LINK, "http://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link test")
        self.assertEqual(html_node.props, { "href" : "http://www.example.com"})

    def test_image_conversion(self):
        text_node = TextNode("image test", TextType.IMAGE, "../images/test.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src" : "../images/test.jpg", "alt" : "image test" })

    def test_invalid_text_type(self):
        text_node = TextNode("test", TextType.TEXT)
        text_node.text_type = "INVALID"
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
