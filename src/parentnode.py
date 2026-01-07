from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag found")
        if self.children == None:
            raise ValueError("No value found")
        
        child_result = ""
        for child in self.children:
            if type(child) is str:
                child_result += child
            else:
                child_result += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{child_result}</{self.tag}>'
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children}, {self.props})"