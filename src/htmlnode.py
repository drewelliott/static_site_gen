from typing import Optional, List, Dict

SELF_CLOSING_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr"
}


class HTMLNode:

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List['HTMLNode']] = None,
        props: Optional[Dict[str, str]] = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props:
            return "".join(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))
        return ""


class LeafNode(HTMLNode):

    def __init__(
        self,
        tag: str,
        value: str,
        props: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag in SELF_CLOSING_TAGS:
            return f"<{self.tag}{self.props_to_html()}/>"
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: List['HTMLNode']) -> None:
        if tag in SELF_CLOSING_TAGS and children:
            raise ValueError(
                f"{tag} is a self-closing tag and cannot have children")
        super().__init__(tag, children=children)

    def to_html(self) -> str:
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        result = [f"<{self.tag}{self.props_to_html()}>"]
        for child in self.children:
            print(child)
            result.append(child.to_html())
        result.append(f"</{self.tag}>")

        return "".join(result)
