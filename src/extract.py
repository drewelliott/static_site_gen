from typing import List, Tuple
import re


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)


def extract_title(markdown: str) -> str:
    lines = markdown.split('\n')

    for line in lines:
        if re.match(r"^([#]{1}\s\w)", line):
            return line.split(' ', 1)[1].strip()

    raise Exception("Main header not found")
