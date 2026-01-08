from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(markdown):
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if markdown.startswith(headings):
        return BlockType.HEADING
    elif markdown.startswith("```\n") and markdown.endswith("```"):
        return BlockType.CODE
    
    split_lines = markdown.split("\n")
    first_char = split_lines[0][0]
    for line in split_lines:
        if line[0] != first_char or line[1] != " ":
            return BlockType.PARAGRAPH
        
    match first_char:
        case ">":
            return BlockType.QUOTE
        case "-":
            return BlockType.UNORDERED_LIST
        case ".":
            return BlockType.ORDERED_LIST
    
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