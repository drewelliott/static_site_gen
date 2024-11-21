import unittest
from src.markdowntoblocks import markdown_to_blocks


class TestMarkdownToText(unittest.TestCase):

    def test_golden_path(self):
        markdown = "# This is a heading.\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        block_list = markdown_to_blocks(markdown)
        expected = [ 
            '# This is a heading.', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        self.assertEqual(expected, block_list)


    def test_single_line_blocks(self):
        markdown = "# This is a heading."
        block_list = markdown_to_blocks(markdown)
        expected = [ 
            '# This is a heading.'
            ]
        self.assertEqual(expected, block_list)



    def test_excessive_blank_lines(self):
        markdown = "# This is a heading.\n\n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n\n\n\n"
        block_list = markdown_to_blocks(markdown)
        expected = [ 
            '# This is a heading.', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]
        self.assertEqual(expected, block_list)



    def test_empty_document(self):
        markdown = ""
        block_list = markdown_to_blocks(markdown)
        expected = [ 
            ]
        self.assertEqual(expected, block_list)



    def text_no_blank_lines(self):
        markdown = "# This is a heading.\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        block_list = markdown_to_blocks(markdown)
        expected = [ 
            "# This is a heading.\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
            ]
        self.assertEqual(expected, block_list)


