from src.markdowntoblocks import markdown_to_blocks
from src.blocktoblocktype import block_to_block_type
from src.htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown: str) -> ParentNode:
    md_blocks = markdown_to_blocks(markdown)

    for block in md_blocks:
        block_type = block_to_block_type(block)
        block_node = LeafNode(block, block_type)
    # Assign the proper child HTMLNode objects to the block node
    # -- I created a shared text_to_children(text) function that 
    # works for all block types. It takes a string of text and returns 
    # a list of HTMLNodes that represent the inline markdown using 
    # previously created functions (think TextNode -> HTMLNode)
    # 
    html_node = ParentNode()

    return html_node