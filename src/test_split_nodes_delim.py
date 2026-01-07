import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_eq(self):
        node = TextNode("This is a text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_begin_eq(self):
        node = TextNode("**Bold** word at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" word at start", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, result)

    def test_split_end_eq(self):
        node = TextNode("Italic word at _end_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result = [
            TextNode("Italic word at ", TextType.TEXT),
            TextNode("end", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, result)

if __name__ == "__main__":
    unittest.main()