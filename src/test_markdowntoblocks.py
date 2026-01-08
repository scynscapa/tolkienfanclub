import unittest
from markdowntoblocks import markdown_to_blocks, block_to_block_type, BlockType

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

. This is a list
. with items
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


if __name__ == "__main__":
    unittest.main()