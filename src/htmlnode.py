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
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value.")
        
        if self.tag is None:
            return self.value
        
        props_str = ''
        if self.props:
            filtered_props = {k: v for k, v in self.props.items() if k is not None and v is not None}
            if filtered_props:
                props_str = ' ' + ' '.join([f'{key}="{value}"' for key, value in filtered_props.items()])
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag.")
        if children is None or not children:
            raise ValueError("ParentNode requires children.")
        
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag.")
        
        if self.children is None or not self.children:
            raise ValueError("ParentNode requires children.")
        
        props_str = ''
        if self.props:
            # the next line creates a new dictionary
            # and filters out any props that have a none value
            # then adds those values to a dictionary which gets
            # concatenated into a string to be fed into the result
            filtered_props = {k: v for k, v in self.props.items() if k is not None and v is not None}
            if filtered_props:
                props_str = ' ' + ' '.join([f'{key}="{value}"' for key, value in filtered_props.items()])
        
        result = f"<{self.tag}{props_str}>"
        for child in self.children:
            if isinstance(child, HTMLNode):
                result += child.to_html()
            else:
                result += str(child)
        return result + f"</{self.tag}>"