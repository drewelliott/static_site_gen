import re

def block_to_block_type(block: str) -> str:

    if re.match(r"^([#]{1,6}\s\w)", block):
        return "heading"

    if re.match(r"^(`{3})(.|\n)*(`{3})$", block):
        return "code"

    block_lines = block.split("\n")
    if all(map(lambda x: bool(re.match(r">{1}.*", x)), block_lines)):
        return "quote"

    if all(map(lambda x: bool(re.match(r"^([\*|\-]\s)", x)), block_lines)):
        return "unordered_list"

    if all(map(lambda x: bool(re.match(r"^([\d]+\.\s)", x)), block_lines)):
        for index, line in enumerate(block_lines, start=1):
            if index != int(line.split(".")[0]):
                return "paragraph"
        return "ordered_list"

    return "paragraph"