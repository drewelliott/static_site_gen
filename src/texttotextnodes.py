from split import split_nodes_link, split_nodes_image, split_nodes_delimiter
from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    new_nodes = []

    # it's important to keep everything in order because we have to recreate the 
    # webpage and if it is all out-of-order then it will make no sense

    # so we will get the indices of each occurrence of a tag in the text string
    # and then sort by them and run each split in the order they are encountered

    # first, to find the indices I will use re.finditer() which will find all
    # indices for each regex in the entire string - each match will have a tuple
    # with the start and end indices for the match - these are accessible in 
    # the result .span()
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    # for the link, we need to make sure we do not match image links, so we have
    # to use the regex "look behind" at the beginning - this says we only want 
    # to match the opening bracket if there is not an exclamation before it
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    bold_regex = "\*\*([^\*]*)\*\*" 
    # we have to use the same tactic for italic or else we would match on all of 
    # the bold markdowns too, but we have to look behind and then also look 
    # ahead to be sure we only have a single asterix
    italic_regex = "(?<!\*)\*([^\*]+)\*(?!\*)" 
    code_regex = "`([^`]+)`"

    # now we are building tuples for each match that includes the starting index
    # followed by the type of match
    image_matches = [(match.span()[0], "image") for match in re.finditer(image_regex, text)]
    link_matches = [(match.span()[0], "link") for match in re.finditer(link_regex, text)]
    bold_matches = [(match.span()[0], "bold") for match in re.finditer(bold_regex, text)]
    italic_matches = [(match.span()[0], "italic") for match in re.finditer(italic_regex, text)]
    code_matches = [(match.span()[0], "code") for match in re.finditer(code_regex, text)]
    
    # now put all matches together and then sort them to get the order that each
    # split needs to happen
    all_matches = image_matches + link_matches + bold_matches + italic_matches + code_matches
    sorted_matches = sorted(all_matches, key=lambda x: x[0])
   
    # turn the string into a textnode
    node = [TextNode(text, TextType.TEXT)]
   
   ## I NEED TO CHECK FOR HOW TO END THIS CORRECTLY
   ## RIGHT NOW IT RUNS TOO MANY TIMES
   # I think I need to add if len(my_nodes) == 3
    for index,match_type in sorted_matches:
        if match_type == 'bold':
            my_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
            if len(my_nodes) == 1:
                new_nodes.extend(my_nodes)
            else:
                new_nodes.extend([my_nodes[0], my_nodes[1]])
                node = [my_nodes[2]]
        elif match_type == 'italic':
            my_nodes = split_nodes_delimiter(node, "*", TextType.ITALIC)
            if len(my_nodes) == 1:
                new_nodes.extend(my_nodes)
            else:
                new_nodes.extend([my_nodes[0], my_nodes[1]])
                node = [my_nodes[2]]
        elif match_type == 'code':
            my_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
            if len(my_nodes) == 1:
                new_nodes.extend(my_nodes)
            else:
                new_nodes.extend([my_nodes[0], my_nodes[1]])
                node = [my_nodes[2]]
        elif match_type == 'image':
            my_nodes = split_nodes_image(node)
            if len(my_nodes) == 1:
                new_nodes.extend(my_nodes)
            else:
                new_nodes.extend([my_nodes[0], my_nodes[1]])
                node = [my_nodes[2]]
        elif match_type == 'link':
            my_nodes = split_nodes_link(node)
            if len(my_nodes) == 1:
                new_nodes.extend(my_nodes)
            else:
                new_nodes.extend([my_nodes[0], my_nodes[1]])
                node = [my_nodes[2]]

    new_nodes.extend(node)

    return new_nodes
