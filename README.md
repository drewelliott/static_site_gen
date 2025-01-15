# static_site_gen

Static Website Generator

This application will find all markdown files in the [content](content) directory and convert those markdown files to html.

To run: `./main.sh` from the main directory.


# Nodes:

    TextNode(TEXT, TEXT_TYPE, URL)
    HTMLNode(TAG, VALUE, [CHILDREN], {PROPS})
    LeafNode(TAG, VALUE, {PROPS})
    ParentNode(TAG, [CHILDREN])

## TextNode

TextNode. It should have 3 properties that can be set in the constructor:

 - self.text - The text content of the node
 - self.text_type - The type of text this node contains, which is a member of the TextType enum.
 - self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

## HTMLNode

HTMLNode class should have 4 data members set in the constructor:

 - tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
 - value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
 - children - A list of HTMLNode objects representing the children of this node
 - props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

Perhaps counterintuitively, every data member should be optional and default to None:

 - An HTMLNode without a tag will just render as raw text
 - An HTMLNode without a value will be assumed to have children
 - An HTMLNode without children will be assumed to have a value
 - An HTMLNode without props simply won't have any attributes

## LeafNode

a child class of HTMLNode called LeafNode. Its constructor should differ slightly from the HTMLNode class because:

 - It should not allow for any children
 - The value data member should be required (and tag even though the tag's value may be None)
 - Use the super() function to call the constructor of the HTMLNode class.

Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).

 - If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
 - If there is no tag (e.g. it's None), the value should be returned as raw text.
 - Otherwise, it should render an HTML tag

## ParentNode

another child class of the HTMLNode called ParentNode. Its constructor should differ from the parent class in that:

 - The tag and children arguments are not optional
 - It doesn't take a value argument
 - props is optional (the exact opposite of the LeafNode class)

Add a .to_html method.

 - If the object doesn't have a tag, raise a ValueError.
 - If children is a missing value, raise a ValueError with a different message.
 - Otherwise, return a string representing the HTML tag of the node and its children. This should be a recursive method (each recursion being called on a nested child node). I iterated over all the children and called to_html on each, concatenating the results and injecting them between the opening and closing tags of the parent.

# Functions

## TextNode to HTMLNode

[textnodetohtmlnode.py](src/textnodetohtmlnode.py)

It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception.

 - TextType.TEXT: This should become a LeafNode with no tag, just a raw text value.
 - TextType.BOLD: This should become a LeafNode with a "b" tag and the text
 - TextType.ITALIC: "i" tag, text
 - TextType.CODE: "code" tag, text
 - TextType.LINK: "a" tag, anchor text, and "href" prop
 - TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

## Split

[split.py](src/split.py)

#### split_nodes_delimiter

It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax.

The beauty of this function is that it will take care of inline code, bold, and italic text, all in one! The logic is identical, the delimiter and matching text_type are the only thing that changes, e.g. ** for bold, * for italic, and a backtick for code. Also, because it operates on an input list, we can call it multiple times to handle different types of delimiters. The order in which you check for different delimiters matters, which actually simplifies implementation.

For simplicity's sake, we won't allow nesting of inline elements! We will only support a single level of nesting when it comes to inline elements. If you want to extend the project to support multiple levels of nesting, you're welcome to do so! But we won't.

#### split_nodes_link

#### split_nodes_image

They should behave very similarly to split_nodes_delimiter, but obviously don't need a delimiter or a text type as input, because they always operate on images or links respectively.

## Extract Links

[extract.py](src/extract.py)

#### extract_markdown_images

a function extract_markdown_images(text) that takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.

#### extract_markdown_links

a similar function extract_markdown_links(text) that extracts markdown links instead of images. It should return tuples of anchor text and URLs.

## Text to TextNodes

[texttotextnodes.py](src/texttotextnodes.py)

#### text_to_textnodes

all the "splitting" functions together into a function that can convert a raw string of markdown-flavored text into a list of TextNode objects.

## Markdown to Blocks

[markdowntoblocks.py](src/markdowntoblocks.py)

Block-level markdown is just the separation of different sections of an entire document. In well-written markdown (which we'll just assume is the only thing going into our generator) blocks are separated by a single blank line.

#### markdown_to_blocks

function called markdown_to_blocks(markdown). It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings.

## Block Types

[blocktoblocktype.py](src/blocktoblocktype.py)

We will support 6 types of markdown blocks:

 - paragraph
 - heading
 - code
 - quote
 - unordered_list
 - ordered_list

#### block_to_block_type

a block_to_block_type function that takes a single block of markdown text as input and returns a string representing the type of block it is. You can assume all leading and trailing whitespace was already stripped (we did that in a previous lesson).

 - Headings start with 1-6 # characters, followed by a space and then the heading text.
 - Code blocks must start with 3 backticks and end with 3 backticks.
 - Every line in a quote block must start with a > character.
 - Every line in an unordered list block must start with a * or - character, followed by a space.
 - Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
 - If none of the above conditions are met, the block is a normal paragraph.

## Block to HTML

#### markdown_to_html

a new function called def markdown_to_html_node(markdown): that converts a full markdown document into a single parent HTMLNode. That one parent HTMLNode should of course contain many child HTMLNode objects representing the nested elements.
