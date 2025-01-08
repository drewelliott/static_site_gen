from src.markdowntoblocks import markdown_to_blocks
from src.blocktoblocktype import block_to_block_type
from src.htmlnode import HTMLNode, LeafNode, ParentNode
from typing import List, Tuple


def markdown_to_html_node(markdown: str) -> ParentNode:
    md_blocks = markdown_to_blocks(markdown)
    children = []

    for block in md_blocks:
        html_nodes = text_to_children(block)
        children.extend(html_nodes)

    html_node = ParentNode("div", children)

    return html_node


def text_to_children(markdown: str) -> List['HTMLNode']:
    html_node_list = []
    block_type = block_to_block_type(markdown)

    if block_type == "heading":
        tag_tuple = parse_heading(markdown)
        html_node_list.append(LeafNode(tag_tuple[0], tag_tuple[1]))

    if block_type == "quote":
        tag_tuple = parse_quote(markdown)
        html_node_list.append(LeafNode(tag_tuple[0], tag_tuple[1]))

    if block_type == "code":
        tag_tuple = parse_code(markdown)
        children = [LeafNode(tag_tuple[1][0], tag_tuple[1][1])]
        html_node_list.append(ParentNode(tag_tuple[0], children))

    if block_type == "unordered_list":
        children = []
        tag_tuple = parse_unordered_list(markdown)
        tag = tag_tuple[0]
        for child in tag_tuple[1]:
            children.append(LeafNode(child[0], child[1]))
        html_node_list.append(ParentNode(tag, children))

    if block_type == "ordered_list":
        children = []
        tag_tuple = parse_ordered_list(markdown)
        tag = tag_tuple[0]
        for child in tag_tuple[1]:
            children.append(LeafNode(child[0], child[1]))
        html_node_list.append(ParentNode(tag, children))

    if block_type == "paragraph":
        html_node_list.append(LeafNode("p", markdown))

    return html_node_list


def parse_heading(markdown: str) -> Tuple[str, str]:
    level, text = markdown.split(' ', 1)

    return (f"h{len(level)}", text)


def parse_quote(markdown: str) -> Tuple[str, str]:
    text = markdown.split(' ', 1)[1]

    return ("blockquote", text)


def parse_code(markdown: str) -> Tuple[str, Tuple[str, str]]:
    lines = markdown.split('\n')

    if lines[0].strip().startswith("```"):
        lines.pop(0)    # remove opening backticks line
    if lines[-1].startswith("```"):
        lines.pop()     # remove the closing backticks line

    code_content = '\n'.join(lines).strip()

    return ("pre", ("code", code_content))


def parse_unordered_list(markdown: str) -> Tuple[str, List[Tuple[str, str]]]:
    list_items = []
    lines = markdown.split('\n')

    for line in lines:
        parts = line.split(' ', 1)
        if len(parts) > 1:
            text = parts[1].strip()
            if text:
                list_items.append(("li", text))

    return ("ul", list_items)


def parse_ordered_list(markdown: str) -> Tuple[str, List[Tuple[str, str]]]:
    list_items = []
    lines = markdown.split('\n')

    for line in lines:
        parts = line.split(' ', 1)
        if parts[0][-1] == '.' and parts[0][:-1].isdigit() and len(parts) > 1:
            text = parts[1].strip()
            if text:
                list_items.append(("li", text))

    return ("ol", list_items)
