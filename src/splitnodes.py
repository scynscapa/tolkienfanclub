from textnode import TextNode, TextType


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