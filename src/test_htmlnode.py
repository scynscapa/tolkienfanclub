import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        test_props = HTMLNode("link", "a", None, props)
        expected = ' href="https://www.google.com" target="_blank"'
        result = test_props.props_to_html()
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()