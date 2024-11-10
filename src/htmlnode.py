
class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return "".join(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))
        return ""


class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):

    def __init__(self, tag, children):
        super().__init__(tag, children=children)

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        result = [f"<{self.tag}>"]
        for child in self.children:
            result.append(child.to_html())
        result.append(f"</{self.tag}>")
            
        return "".join(result) 
