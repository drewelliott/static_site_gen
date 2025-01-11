import unittest
from src.extract import (
    extract_markdown_images,
    extract_markdown_links,
    extract_title
)


class TestExtract(unittest.TestCase):

    def test_extract_one_image(self):
        text = "This is text with a ![first](http://first.example.com)"
        result = extract_markdown_images(text)
        expected = [('first', 'http://first.example.com')]
        self.assertEqual(result, expected)

    def test_extract_two_images(self):
        text = "This is text with a ![first](http://first.example.com) and ![second](https://second.example.com)"
        result = extract_markdown_images(text)
        expected = [('first', 'http://first.example.com'),
                    ('second', 'https://second.example.com')]
        self.assertEqual(result, expected)

    def test_extract_three_images(self):
        text = "This is text with a ![first](http://first.example.com) and ![second](https://second.example.com) and ![third](https://third.example.com)"
        result = extract_markdown_images(text)
        expected = [('first', 'http://first.example.com'),
                    ('second', 'https://second.example.com'),
                    ('third', 'https://third.example.com')]
        self.assertEqual(result, expected)

    def test_extract_one_link(self):
        text = "This is text with a [first](http://first.example.com)"
        result = extract_markdown_links(text)
        expected = [('first', 'http://first.example.com')]
        self.assertEqual(result, expected)

    def test_extract_two_links(self):
        text = "This is text with a [first](http://first.example.com) and [second](https://second.example.com)"
        result = extract_markdown_links(text)
        expected = [('first', 'http://first.example.com'),
                    ('second', 'https://second.example.com')]
        self.assertEqual(result, expected)

    def test_extract_three(self):
        text = "This is text with a [first](http://first.example.com) and [second](https://second.example.com) and [third](https://third.example.com)"
        result = extract_markdown_links(text)
        expected = [('first', 'http://first.example.com'),
                    ('second', 'https://second.example.com'),
                    ('third', 'https://third.example.com')]
        self.assertEqual(result, expected)

    def test_extract_title_golden(self):
        markdown = "# Heading\nSome content"
        result = extract_title(markdown)
        expected = "Heading"
        self.assertEqual(result, expected)

    def test_extract_title_missing_header(self):
        markdown = "Heading\nSome content"

        with self.assertRaises(Exception) as exc_info:
            extract_title(markdown)

        self.assertEqual(str(exc_info.exception), "Main header not found")

    def test_extract_title_special_char(self):
        markdown = "# Heading !!\nSome content"
        result = extract_title(markdown)
        expected = "Heading !!"
        self.assertEqual(result, expected)

    def test_extract_title_extra_space(self):
        markdown = "# Heading  \nSome content"
        result = extract_title(markdown)
        expected = "Heading"
        self.assertEqual(result, expected)

    def test_extract_title_bad_markdown(self):
        markdown = "#Heading\nSome content"

        with self.assertRaises(Exception) as exc_info:
            extract_title(markdown)

        self.assertEqual(str(exc_info.exception), "Main header not found")

    def test_extract_title_not_h1(self):
        markdown = "## Heading\nSome content"

        with self.assertRaises(Exception) as exc_info:
            extract_title(markdown)

        self.assertEqual(str(exc_info.exception), "Main header not found")
