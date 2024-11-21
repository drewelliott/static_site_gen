from src.textnode import TextType, TextNode
from src.extract import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        else:
            start = node.text.find(delimiter)
            if start == -1:
                new_nodes.append(node)
                continue

            end = node.text.find(delimiter, start + len(delimiter))
            if end == -1:
                raise ValueError("Invalid markdown syntax")

            node0 = TextNode(node.text[:start], TextType.TEXT)
            node1 = TextNode(node.text[start + len(delimiter):end], text_type)
            node2 = TextNode(node.text[end + len(delimiter):], TextType.TEXT)

            new_nodes.extend([ node0, node1 ])
            new_nodes.extend(split_nodes_delimiter([node2], delimiter, text_type))

    return new_nodes
            

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_links = extract_markdown_links(node.text)
        # initialize string position index
        pos = 0

        for alt, url in extracted_links:
            link_syntax = f"[{alt}]({url})"
            # find string index where the link starts
            start = node.text.find(link_syntax, pos)

            # if the start of the link is greater than the current position index, then 
            # we know there is leading text that needs to be added to new_nodes
            if start > pos:
                new_nodes.append(TextNode(node.text[pos:start], TextType.TEXT))

            # now we need to append the link to new_nodes
            new_nodes.append(TextNode(alt, TextType.LINK, url))

            # now we need to update our position, so we add the start position of the
            # link to our position so that we are now positioned at the end of the last 
            # link in the string
            pos = start + len(link_syntax)

        # now we need to add any remaining text after the last link was found
        if pos < len(node.text):
            new_nodes.append(TextNode(node.text[pos:], TextType.TEXT))

    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_image_links = extract_markdown_images(node.text)
        # initialize string position index
        pos = 0

        for alt, url in extracted_image_links:
            link_syntax = f"![{alt}]({url})"
            # find string index where the image link starts
            start = node.text.find(link_syntax, pos)

            # if the start of the link is greater than the current position index, then 
            # we know there is leading text that needs to be added to new_nodes
            if start > pos:
                new_nodes.append(TextNode(node.text[pos:start], TextType.TEXT))

            # now we need to append the image to new_nodes
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))


            # now we need to update our position, so we add the start position of the
            # link to our position so that we are now positioned at the end of the last 
            # link in the string
            pos = start + len(link_syntax)

        # now we need to add any remaining text after the last link was found
        if pos < len(node.text):
            new_nodes.append(TextNode(node.text[pos:], TextType.TEXT))

    return new_nodes
