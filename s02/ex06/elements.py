class Elem:
    def __init__(self, elms=[], name: str = "element", attrs: dict[str, str] = {}, is_simple: bool = False):
        self.name = name
        self.elms = elms
        attributes = ''
        for key,val in attrs.items():
            attributes += f' {key}="{val}"'
        if is_simple:
            self.el = f'<{name}{attributes}>'
        else:
            self.el = f'<{name}{attributes}>' + '{content}' + f'</{name}>'

    def __str__(self) -> str:
        content = ""
        for el in self.elms:
            content += str(el)
        element = self.el
        result = element.format(content=content)
        return result
    
    def add_content(self, *els, is_after = False):
        content = ''
        if isinstance(els, str):
            content = els
        else:
            for el in els:
                content += str(el)
        if is_after:
            self.el += content
        else:
            self.el = self.el.format(content=content)
        return self

    class ElemException(Exception):
        def __init__(self, *args: object):
            super().__init__(*args)

class Html(Elem):
    def __init__(self, elms=[], name = "html", attrs={}, is_simple=False):
        super().__init__(elms, name, attrs, is_simple)

class Head(Elem):
    def __init__(self, elms=[], name: str = "head", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Body(Elem):
    def __init__(self, elms=[], name: str = "body", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Title(Elem):
    def __init__(self, elms=[], name: str = "title", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Meta(Elem):
    def __init__(self, elms=[], name: str = "meta", attrs: dict[str, str] = {}, is_simple: bool = True):
        super().__init__(elms, name, attrs, is_simple)

class Img(Elem):
    def __init__(self, elms=[], name: str = "img", attrs: dict[str, str] = {}, is_simple: bool = True):
        super().__init__(elms, name, attrs, is_simple)

class Table(Elem):
    def __init__(self, elms=[], name: str = "table", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Th(Elem):
    def __init__(self, elms=[], name: str = "th", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Tr(Elem):
    def __init__(self, elms=[], name: str = "tr", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Td(Elem):
    def __init__(self, elms=[], name: str = "td", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Ul(Elem):
    def __init__(self, elms=[], name: str = "ul", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Ol(Elem):
    def __init__(self, elms=[], name: str = "ol", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Li(Elem):
    def __init__(self, elms=[], name: str = "li", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class H1(Elem):
    def __init__(self, elms=[], name: str = "h1", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class H2(Elem):
    def __init__(self, elms=[], name: str = "h2", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class P(Elem):
    def __init__(self, elms=[], name: str = "p", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Div(Elem):
    def __init__(self, elms=[], name: str = "div", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Span(Elem):
    def __init__(self, elms=[], name: str = "span", attrs: dict[str, str] = {}, is_simple: bool = False):
        super().__init__(elms, name, attrs, is_simple)

class Hr(Elem):
    def __init__(self, elms=[], name: str = "hr", attrs: dict[str, str] = {}, is_simple: bool = True):
        super().__init__(elms, name, attrs, is_simple)

class Br(Elem):
    def __init__(self, elms=[], name: str = "br", attrs: dict[str, str] = {}, is_simple: bool = True):
        super().__init__(elms, name, attrs, is_simple)