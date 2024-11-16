import unittest
from textnode import TextNode, TextType
from split import split_nodes_link, split_nodes_image

class TestSplitNodeLink(unittest.TestCase):
   
    def test_non_text_node(self):
        node = [
                TextNode("to yahoo", TextType.LINK, "https://www.yahoo.com")
                ]
        new_nodes = split_nodes_link(node)
        expected = [
                TextNode(text="to yahoo", text_type=TextType.LINK, url="https://www.yahoo.com")
                ]
        self.assertEqual(expected, new_nodes)

    def test_image_node(self):
        node = [
                TextNode("This is text with a link ![to boot dev](images/boot_dev.jpg).", TextType.TEXT)
                ]
        new_nodes = split_nodes_link(node)
        expected = [
                TextNode("This is text with a link ![to boot dev](images/boot_dev.jpg).", TextType.TEXT)
                    ]
        self.assertEqual(expected, new_nodes)

    def test_four_nodes_non_single_double_triple(self):
        nodes = [
            TextNode("to yahoo", TextType.LINK, "https://www.yahoo.com"),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) ending.", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev).", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and even more [yahoo!](https://yahoo.com)", TextType.TEXT)
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="to yahoo", text_type=TextType.LINK, url="https://www.yahoo.com"),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" ending.", text_type=TextType.TEXT, url=None),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=".", text_type=TextType.TEXT, url=None),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=" and even more ", text_type=TextType.TEXT, url=None),
            TextNode(text="yahoo!", text_type=TextType.LINK, url="https://yahoo.com")
            ]
        self.assertEqual(expected, new_nodes)


    def test_single_link(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) ending.", TextType.TEXT),
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" ending.", text_type=TextType.TEXT, url=None)
            ]
        self.assertEqual(expected, new_nodes)


    def test_double_link(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) ending.", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev).", TextType.TEXT),
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" ending.", text_type=TextType.TEXT, url=None),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=".", text_type=TextType.TEXT, url=None)
            ]
        self.assertEqual(expected, new_nodes)


    def test_triple_link(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) ending.", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev).", TextType.TEXT),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and even more [yahoo!](https://yahoo.com)", TextType.TEXT)
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" ending.", text_type=TextType.TEXT, url=None),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=".", text_type=TextType.TEXT, url=None),
            TextNode(text="This is text with a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" and ", text_type=TextType.TEXT, url=None),
            TextNode(text="to youtube", text_type=TextType.LINK, url="https://www.youtube.com/@bootdotdev"),
            TextNode(text=" and even more ", text_type=TextType.TEXT, url=None),
            TextNode(text="yahoo!", text_type=TextType.LINK, url="https://yahoo.com")
            ]
        self.assertEqual(expected, new_nodes)


    def test_link_no_leading_text(self):
        nodes = [
            TextNode("[to boot dev](https://www.boot.dev) This is text after a link.", TextType.TEXT)
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev"),
            TextNode(text=" This is text after a link.", text_type=TextType.TEXT, url=None)
            ]
        self.assertEqual(expected, new_nodes)


    def test_link_no_trailing_text(self):
        nodes = [
            TextNode("This is text before a link [to boot dev](https://www.boot.dev)", TextType.TEXT),
            ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode(text="This is text before a link ", text_type=TextType.TEXT, url=None),
            TextNode(text="to boot dev", text_type=TextType.LINK, url="https://www.boot.dev")
            ]
        self.assertEqual(expected, new_nodes)

        
