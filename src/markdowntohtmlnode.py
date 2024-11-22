from src.markdowntoblocks import markdown_to_blocks
from src.blocktoblocktype import block_to_block_type
from src.htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    # split the markdown into blocks
    #
    # loop over each block
    # determine the type of block
    # create new HTMLNode based on the type of block
    # Assign the proper child HTMLNode objects to the block node
    # -- I created a shared text_to_children(text) function that 
    # works for all block types. It takes a string of text and returns 
    # a list of HTMLNodes that represent the inline markdown using 
    # previously created functions (think TextNode -> HTMLNode)
    # 
    html_node = ParentNode()

    return html_node