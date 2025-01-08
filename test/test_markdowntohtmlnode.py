import unittest
from src.htmlnode import ParentNode, LeafNode
from src.markdowntohtmlnode import (
    markdown_to_html_node,
    parse_heading,
    parse_quote,
    parse_code,
    parse_unordered_list,
    parse_ordered_list
)


class TestMarkdownToHTML(unittest.TestCase):

    def test_parse_heading(self):
        # Tests for heading parsing
        md = "# This is a heading"
        expected = ("h1", "This is a heading")
        result = parse_heading(md)
        self.assertEqual(result, expected)

    def test_parse_heading_six(self):
        # Tests for heading parsing
        md = "###### This is a heading"
        expected = ("h6", "This is a heading")
        result = parse_heading(md)
        self.assertEqual(result, expected)

    def test_parse_quote(self):
        # Tests for blockquote parsing
        md = "> This is a quote"
        expected = ("blockquote", "This is a quote")
        result = parse_quote(md)
        self.assertEqual(result, expected)

    def test_parse_code(self):
        # Tests for code block parsing
        md = """```
print("Hello World")
```"""
        expected = ("pre", ("code", 'print("Hello World")'))
        result = parse_code(md)
        self.assertEqual(result, expected)

    def test_parse_unordered_list(self):
        # Tests for unordered list parsing
        md = "- Item one\n- Item two"
        expected = ("ul", [("li", "Item one"), ("li", "Item two")])
        result = parse_unordered_list(md)
        self.assertEqual(result, expected)

    def test_parse_ordered_list(self):
        # Tests for ordered list parsing
        md = "1. First\n2. Second"
        expected = ("ol", [("li", "First"), ("li", "Second")])
        result = parse_ordered_list(md)
        self.assertEqual(result, expected)

    def test_markdown_to_html_node(self):
        md = """
# Heading

> Quote

Paragraph

- Item 1
- Item 2

```python
print("Hello, World!")
```

1. Item 1
2. Item 2"""

        result = markdown_to_html_node(md)

        self.assertIsInstance(result, ParentNode)

        self.assertEqual(result.tag, "div")

        children = result.children
        self.assertEqual(len(children), 6)

        heading_node = children[0]
        self.assertIsInstance(heading_node, LeafNode)
        self.assertEqual(heading_node.tag, "h1")
        self.assertEqual(heading_node.value, "Heading")

        quote_node = children[1]
        self.assertIsInstance(quote_node, LeafNode)
        self.assertEqual(quote_node.tag, "blockquote")
        self.assertEqual(quote_node.value, "Quote")

        paragraph_node = children[2]
        self.assertIsInstance(paragraph_node, LeafNode)
        self.assertEqual(paragraph_node.tag, "p")
        self.assertEqual(paragraph_node.value, "Paragraph")

        ulist_node = children[3]
        self.assertIsInstance(ulist_node, ParentNode)
        self.assertEqual(ulist_node.tag, "ul")

        ulist_items = ulist_node.children
        self.assertEqual(len(ulist_items), 2)

        ulitem_1 = ulist_items[0]
        self.assertIsInstance(ulitem_1, LeafNode)
        self.assertEqual(ulitem_1.tag, "li")
        self.assertEqual(ulitem_1.value, "Item 1")

        ulitem_2 = ulist_items[1]
        self.assertIsInstance(ulitem_2, LeafNode)
        self.assertEqual(ulitem_2.tag, "li")
        self.assertEqual(ulitem_2.value, "Item 2")

        code_node = children[4]
        self.assertIsInstance(code_node, ParentNode)
        self.assertEqual(code_node.tag, "pre")

        code_items = code_node.children
        self.assertEqual(len(code_items), 1)

        code_1 = code_items[0]
        self.assertIsInstance(code_1, LeafNode)
        self.assertEqual(code_1.tag, "code")
        self.assertEqual(code_1.value, 'print("Hello, World!")')

        olist_node = children[5]
        self.assertIsInstance(olist_node, ParentNode)
        self.assertEqual(olist_node.tag, "ol")

        olist_items = olist_node.children
        self.assertEqual(len(olist_items), 2)

        olitem_1 = olist_items[0]
        self.assertIsInstance(olitem_1, LeafNode)
        self.assertEqual(olitem_1.tag, "li")
        self.assertEqual(olitem_1.value, "Item 1")

        olitem_2 = olist_items[1]
        self.assertIsInstance(olitem_2, LeafNode)
        self.assertEqual(olitem_2.tag, "li")
        self.assertEqual(olitem_2.value, "Item 2")


if __name__ == "__main__":
    unittest.main()
