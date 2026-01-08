from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = list()

    for node in old_nodes:
        #if text_type is not TextType.TEXT:
         #   result.append(node.text)
        
        # make sure delimiters are balanced
        delim_count = 0
        for char in node.text:
            if char is delimiter:
                delim_count += 1
        if delim_count % 2 != 0:
            raise Exception("Invalid Markdown syntax: delimiter not closed")
        
        node_text = node.text.split(delimiter)
        match delimiter:
            case "`":
                node_type = TextType.CODE
            case "_":
                node_type = TextType.ITALIC
            case "**":
                node_type = TextType.BOLD
            
        if node.text.startswith(delimiter) and len(node_text) == 3:
            result.append(TextNode(node_text[1], node_type))
            result.append(TextNode(node_text[2], TextType.TEXT))
        elif node.text.endswith(delimiter) and len(node_text) == 3:
            result.append(TextNode(node_text[0], TextType.TEXT))
            result.append(TextNode(node_text[1], node_type))
        else:
            result.append(TextNode(node_text[0], TextType.TEXT))
            result.append(TextNode(node_text[1], node_type))
            result.append(TextNode(node_text[2], TextType.TEXT))

    return result

def split_nodes_image(old_nodes):
    result = list()

    for node in old_nodes:
        remaining_text = node.text
        
        for image_alt, image_url in extract_markdown_images(remaining_text):
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
                
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            remaining_text = sections[1]

    return result



def split_nodes_link(old_nodes):
    result = list()

    for node in old_nodes:
        remaining_text = node.text
        
        for link_text, link_url in extract_markdown_links(remaining_text):
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = sections[1]

    return result
