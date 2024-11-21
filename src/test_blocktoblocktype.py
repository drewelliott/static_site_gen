import unittest
from blocktoblocktype import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading_golden(self):
        block = "# This is a heading." 
        block_type = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(block_type, expected)
        
    def test_heading_leading_space(self):
        block = " # This is a heading." 
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)
        
    def test_heading_six(self):
        block = "###### This is a heading." 
        block_type = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(block_type, expected)

    def test_heading_seven(self):
        block = "####### This is a heading." 
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_code_golden(self):
        block = "``` This is a code block ```"
        block_type = block_to_block_type(block)
        expected = "code"
        self.assertEqual(block_type, expected)

    def test_code_with_line_breaks(self):
        block = "``` This is a\n code\n block\n\n\n ```"
        block_type = block_to_block_type(block)
        expected = "code"
        self.assertEqual(block_type, expected)

    def test_code_without_spaces(self):
        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        expected = "code"
        self.assertEqual(block_type, expected)

    def test_code_with_leading_space(self):
        block = " ```This is a code block```"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_code_with_trailing_space(self):
        block = "```This is a code block``` "
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_quote_golden(self):
        block = ">This is a quote block"
        block_type = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(block_type, expected)

    def test_quote_multiline(self):
        block = ">This is a quote block\n>with multiple\n>lines"
        block_type = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(block_type, expected)

    def test_quote_leading_space(self):
        block = " >This is a quote block"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_quote_multiline_leading_space(self):
        block = ">This is a quote block\n >This one has leading space"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_quote_excessive_newlines(self):
        block = ">This is a quote block\n\n\n>After excessive newlines"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected)

    def test_unordered_list_golden_dash(self):
        block = "- item 1\n- item 2\n- item 3"
        block_type = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(block_type, expected) 

    def test_unordered_list_golden_star(self):
        block = "* item 1\n* item 2\n* item 3"
        block_type = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(block_type, expected) 

    def test_unordered_list_golden_mixed(self):
        block = "- item 1\n* item 2\n- item 3"
        block_type = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(block_type, expected) 

    def test_unordered_list_no_space(self):
        block = "-item 1\n* item 2\n- item 3"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_unordered_list_excessive_newlines(self):
        block = "- item 1\n\n- item 2\n- item 3"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_unordered_list_leading_space(self):
        block = " - item 1\n- item 2\n- item 3"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_ordered_list_golden(self):
        block = "1. item one\n2. item two\n3. item three"
        block_type = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(block_type, expected) 

    def test_ordered_list_no_space_first_item(self):
        block = "1.item one\n2. item two\n3. item three"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_ordered_list_no_space_last_item(self):
        block = "1. item one\n2. item two\n3.item three"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_ordered_list_excessive_newlines(self):
        block = "1. item one\n\n2. item two\n3. item three"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 

    def test_ordered_list_leading_space(self):
        block = " 1. item one\n2. item two\n3. item three"
        block_type = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(block_type, expected) 
