from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node
from texttotextnodes import text_to_textnodes
from textnode import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode
from parentnode import ParentNode
import re

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    result = ""
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.CODE:
                text = block.lstrip("```\n").rstrip("```")
                text_node = TextNode(text, TextType.CODE)
                node = text_node_to_html_node(text_node)
                node = ParentNode("pre", node.to_html())

            case BlockType.PARAGRAPH:
                tag = "p"
                lines = block.split("\n")
                paragraph = " ".join(lines)
                children = text_to_children(paragraph)
                node = ParentNode(tag, children)

            case BlockType.HEADING:
                count = block.count("#")
                if count < 1 or count > 6:
                    continue
                tag = f"h{count}"
                text = re.sub(r'^#+ ', '', block)
                node = LeafNode(tag, text)

            case BlockType.QUOTE:
                tag = "blockquote"
                lines = block.split("\n")
                list_lines = list()
                for line in lines:
                    line = line.lstrip("> ")
                    list_lines.append(line)
                text = "\n".join(list_lines)
                children = text_to_children(text)
                node = ParentNode(tag, children)

            case BlockType.UNORDERED_LIST:
                tag = "ul"
                subtag = "li"
                list_items = list()
                lines = block.split("\n")
                for line in lines:
                    line = line.lstrip("- ")
                    children = text_to_children(line)
                    inner_node = ParentNode(subtag, children)
                    list_items.append(inner_node)
                node = ParentNode(tag, list_items)

            case BlockType.ORDERED_LIST:
                tag = "ol"
                subtag = "li"
                list_items = list()
                lines = block.split("\n")
                for line in lines:
                    line = re.sub(r'^\d+\. ', '', line)
                    children = text_to_children(line)
                    inner_node = ParentNode(subtag, children)
                    list_items.append(inner_node)
                node = ParentNode(tag, list_items)
        
        result += node.to_html()
    return ParentNode("div", result)
        
def text_to_children(text):
    result = list()
    nodes = text_to_textnodes(text)
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return result


def block_to_block_type(markdown):
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if markdown.startswith(headings):
        return BlockType.HEADING
    elif markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    
    split_lines = markdown.split("\n")
    
    # check for ordered list: number at start followed by period
    pattern = r"^\d+\."
    if re.match(pattern, split_lines[0]):
        return BlockType.ORDERED_LIST
    
    first_char = split_lines[0][0]
    for line in split_lines:
        if line[0] != first_char and line[1] == " ":
            return BlockType.PARAGRAPH
        
    match first_char:
        case ">":
            return BlockType.QUOTE
        case "-":
            return BlockType.UNORDERED_LIST
        # case ".":
        #     return BlockType.ORDERED_LIST
    
    
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = list()

    for block in blocks:
        temp_block = block.strip()
        if temp_block == "":
            continue
        result.append(temp_block)
    
    return result