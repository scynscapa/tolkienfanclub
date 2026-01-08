import unittest
from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        results = list()
        for block in blocks:
             results.append(block_to_block_type(block))
        self.assertEqual(
            results,
            [
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST
            ]
        )

    def test_block_to_block_type_1(self):
        md = """
# This is **bolded** paragraph

> This is another paragraph with _italic_ text and `code` here
> This is the same paragraph on a new line

1. This is a list
2. with items
"""
        blocks = markdown_to_blocks(md)
        results = list()
        for block in blocks:
             results.append(block_to_block_type(block))
        self.assertEqual(
            results,
            [
                BlockType.HEADING,
                BlockType.QUOTE,
                BlockType.ORDERED_LIST
            ]
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# A single heading

### A triple heading

###### A heading with six
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>A single heading</h1><h3>A triple heading</h3><h6>A heading with six</h6></div>"
        )

    def test_unorderedlist(self):
        md = """
- List item 1
- List item 2
- List item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List item 1</li><li>List item 2</li><li>List item 3</li></ul></div>"
        )

    def test_orderedlist(self):
        md = """
1. List item 1
5. List item 5
10. List item 10
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>List item 1</li><li>List item 5</li><li>List item 10</li></ol></div>"
        )
        


if __name__ == "__main__":
    unittest.main()