import unittest
from extract import extract_markdown_images, extract_markdown_links

class TestExtract(unittest.TestCase):

    def test_extract_one_image(self):
        text = "This is text with a ![first](http://first.example.com)"
        result = extract_markdown_images(text)
        expected = [('first', 'http://first.example.com')]
        self.assertEqual(result, expected)

    def test_extract_two_images(self):
        text = "This is text with a ![first](http://first.example.com) and ![second](https://second.example.com)"
        result = extract_markdown_images(text)
        expected =  expected = [('first', 'http://first.example.com'),('second', 'https://second.example.com')]
        self.assertEqual(result, expected)

    def test_extract_three_images(self):
        text = "This is text with a ![first](http://first.example.com) and ![second](https://second.example.com) and ![third](https://third.example.com)"
        result = extract_markdown_images(text)
        expected =  expected = [('first', 'http://first.example.com'),('second', 'https://second.example.com'),('third', 'https://third.example.com')]
        self.assertEqual(result, expected)

    def test_extract_one_link(self):
        text = "This is text with a [first](http://first.example.com)"
        result = extract_markdown_links(text)
        expected = [('first', 'http://first.example.com')]
        self.assertEqual(result, expected)

    def test_extract_two_links(self):
        text = "This is text with a [first](http://first.example.com) and [second](https://second.example.com)"
        result = extract_markdown_links(text)
        expected =  expected = [('first', 'http://first.example.com'),('second', 'https://second.example.com')]
        self.assertEqual(result, expected)

    def test_extract_three(self):
        text = "This is text with a [first](http://first.example.com) and [second](https://second.example.com) and [third](https://third.example.com)"
        result = extract_markdown_links(text)
        expected =  expected = [('first', 'http://first.example.com'),('second', 'https://second.example.com'),('third', 'https://third.example.com')]
        self.assertEqual(result, expected)

