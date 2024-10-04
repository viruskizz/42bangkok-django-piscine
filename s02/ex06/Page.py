class Elem:
    def __init__(self, elms=[], name: str = "element", attrs: dict[str, str] = {}, is_simple: bool = False):
        self.name = name
        if not isinstance(elms, list):
            raise self.ElemException("Elements type is not list")
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

class Text(Elem):
    def __init__(self, elms=[], name: str = "text", attrs: dict[str, str] = {}, is_simple: bool = True):
        super().__init__(elms, name, attrs, is_simple)

class Page:
    def __init__(self, el: Elem) -> None:
        self.el = el
        self.__valid_tag = {
            'Html',
            'Head',
            'Body',
            'Title',
            'Meta',
            'Img',
            'Table',
            'Th',
            'Tr',
            'Td' , 
            'Ul',
            'Ol',
            'Li',
            'H1',
            'H2',
            'P',
            'Div',
            'Span',
            'Hr',
            'Dr',
            'Text'
        }
        self.__valid_div = {
            'H1',
            'H2',
            'Div',
            'Table',
            'Ul',
            'Ol',
            'Span',
            'Text',
            'Div'
        }
    # def __str__(self) -> str:
    #     return self.el

    def is_valid(self):
        option = {
            'body': False,
            'title': False,
            'div': False,
        }
        if not self.is_head_body_valid() or not self.is_tag_valid(option):
            return False
        return True

    def is_tag_valid(self, option) -> bool:
        classname = self.el.__class__.__name__
        if classname == 'Body':
            option['body'] = True
        if classname == 'Div':
            option['div'] = True
        if classname == 'Title' or classname == 'H1' or classname == 'H2' or classname == 'Li' or classname == 'Th' or classname == 'Td' or classname == 'Text':
            option['title'] = True
        for el in self.el.elms:
            cname = el.__class__.__name__
            if cname not in self.__valid_tag:
                return False
            if (cname == 'Body' or cname == 'Div') and not self.is_valid_div(el.elms):
                return False
            if cname == 'Title' and el.elms and len(el.elms) != 1 and el.elm[0].__class_.__name__ == 'Text':
                return False
            if cname == 'P' and not self.is_only_text(el.elms):
                return False
            if cname == 'Span' and not self.is_only_ptext(el.elms):
                return False
            if (cname == 'Ul' or cname == 'Ol') and not self.is_some_li(el.elms):
                return False
            if cname == 'Table' and not self.is_some_tr(el.elms):
                return False
            if cname == 'Tr' and not self.is_some_thd(el.elms):
                return False
            if len(el.elms) > 0:
                if not Page(el).is_tag_valid(option):
                    return False
        return (True)
    
    def is_head_body_valid(self) -> bool:
        if self.el.__class__.__name__ != 'Html':
            return False
        elms = self.el.elms
        if len(elms) != 2 or \
            elms[0].__class__.__name__ != 'Head' or \
            elms[1].__class__.__name__ != 'Body':
            return False
        if not self.is_only_title(elms[0].elms):
            return False
        return True

    def is_only_title(self, elms) -> bool:
        count = 0
        for el in elms:
            if el.__class__.__name__ == 'Title':
                count += 1
        if count != 1:
            return False
        return True

    def is_only_text(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Text':
                return False
        return True

    def is_only_ptext(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Text' and el.__class__.__name__ != 'P':
                return False
        return True
    
    def is_some_li(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Li':
                return False
        return len(elms) >= 1

    def is_some_thd(self, elms) -> bool:
        if len(elms) == 0:
            return False
        cur = elms[0].__class__.__name__
        if cur != 'Th' and cur != 'Td':
            return False
        for el in elms:
            if el.__class__.__name__ != cur:
                return False
        return True

    def is_some_tr(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Tr':
                return False
        return True

    def is_valid_div(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ not in self.__valid_div:
                return False
        return True
