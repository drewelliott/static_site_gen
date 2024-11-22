from enum import Enum
from typing import Optional

class NodeType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"


class TextNode:

    def __init__(
        self, 
        text: str, 
        text_type: TextType, 
        url: Optional[str] = None
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and \
                (self.text_type == other.text_type) and \
                (self.url == other.url)

    def __repr__(self):
        return f"TextNode(text={self.text}, text_type={self.text_type}, url={self.url})"
