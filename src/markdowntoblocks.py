
def markdown_to_blocks(markdown):
    block_list = []
    md_list = markdown.split("\n\n")
    for item in md_list:
        if item.strip():
            block_list.append(item.strip())

    return block_list