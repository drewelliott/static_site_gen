
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
