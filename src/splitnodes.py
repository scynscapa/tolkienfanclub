from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    result = list()

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            result.append(node)
            continue        
        remaining_text = node.text
        
        for image_alt, image_url in extract_markdown_images(remaining_text):
            sections = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result



def split_nodes_link(old_nodes):
    result = list()

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            result.append(node)
            continue
        
        remaining_text = node.text
        
        for link_text, link_url in extract_markdown_links(remaining_text):
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = sections[1]
        if remaining_text != "":
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result
