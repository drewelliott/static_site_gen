from split import (
    split_nodes_link,
    split_nodes_image,
    split_nodes_delimiter
)
from textnode import TextType, TextNode
from typing import List


def text_to_textnodes(text: str) -> List[TextNode]:

    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes
