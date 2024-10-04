class Elem:
    def __init__(self, name, attrs = {}, is_simple = False) -> None:
        self.name = name
        attributes = ''
        for key,val in attrs.items():
            attributes += f' {key}="{val}"'
        if is_simple:
            self.el = f'<{name}{attributes}>'
        else:
            self.el = f'<{name}{attributes}>' + '{content}' + f'</{name}>'
    
    def __str__(self) -> str:
        result = self.el.format(content="")
        return result
    
    def add_content(self, *els, is_after = False):
        content = ''
        if type(els) is str:
            content = els
        else:
            for el in els:
                content += str(el)
        if is_after:
            self.el += content
        else:
            self.el = self.el.format(content=content)

    class ElemException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)