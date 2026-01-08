import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
            


if __name__ == "__main__":
    unittest.main()