from typing import List

def markdown_to_blocks(markdown: str) -> List[str]:
    """Split markdown into blocks separated by newlines.
    
    Current limitations:
    - Assumes code blocks don't contain blank lines
    - Assumes well-formatted markdown with single newlines between blocks
    
    Future improvements needed:
    - Handle code blocks (```) containing blank lines without splitting them
    - Handle variable numbers of blank lines between blocks
    - Handle inconsistent whitespace/indentation
    """
    block_list = []
    md_list = markdown.split("\n\n")
    for item in md_list:
        if item.strip():
            block_list.append(item.strip())

    return block_list