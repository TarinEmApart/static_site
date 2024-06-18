class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        result = ''
        for key, value in self.props.items():
            result += f" {key}=\"{value}\"" 
        return result
        
    def __repr__(self):
        print(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value.")
        
        if self.tag is None:
            return self.value
        
        props_str = ''
        if self.props: #checks that self.props is not none and not empty
            props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
