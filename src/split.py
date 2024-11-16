from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        else:
            split_node = node.text.split(delimiter)
            if len(split_node) < 3:
                raise ValueError("Invalid markdown syntax")

            new_nodes.extend([
                TextNode(split_node[0], TextType.TEXT),
                TextNode(split_node[1], text_type),
                TextNode(split_node[2], TextType.TEXT)
            ])

    return new_nodes
        
