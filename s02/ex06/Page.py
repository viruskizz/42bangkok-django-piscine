class Elem:
    def __init__(self, elms=[], name: str = "element", attrs: dict[str, str] = {}, is_simple: bool = False):
        self.name = name
        if not isinstance(elms, list):
            self.elms = [elms]
        else:
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

class Text():
    def __init__(self, text = ""):
        self.text = text
        self.elms=[]
    
    def __str__(self) -> str:
        return self.text

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

    def __str__(self) -> str:
        doc = '<!DOCTYPE html>'
        return doc + str(self.el)

    def is_valid(self):
        if self.el.__class__.__name__ != 'Html':
            return False
        if not self.__is_head_body(self.el.elms):
            return False
        return self.__is_tag_valid()

    def write_to_file(self, filename):
        f = open(filename, "w")
        f.write(str(self))
        f.close()


    def __is_tag_valid(self) -> bool:
        for el in self.el.elms:
            cname = el.__class__.__name__
            if cname not in self.__valid_tag:
                return False
            if (cname == 'Body' or cname == 'Div') and not self.__is_valid_div(el.elms):
                print("Invalid: Body and Div")
                return False
            if cname == 'Head' and not self.__is_only_title(el.elms):
                print("Invalid: Head")
                return False
            if cname in {'Title', 'H1', 'H2', 'Li', 'Th', 'Td'} and not self.__is_single_text(el.elms):
                print(f'Invalid: {cname} need only single Text')
                return False
            if cname == 'P' and not self.__is_only_text(el.elms):
                print("Invalid: P")
                return False
            if cname == 'Span' and not self.__is_only_ptext(el.elms):
                return False
            if (cname == 'Ul' or cname == 'Ol') and not self.__is_some_li(el.elms):
                return False
            if cname == 'Table' and not self.__is_some_tr(el.elms):
                return False
            if cname == 'Tr' and not self.__is_some_thd(el.elms):
                return False
            if len(el.elms) > 0:
                if not Page(el).__is_tag_valid():
                    return False
        return (True)

    def __is_head_body(self, elms) -> bool:
        if len(elms) != 2:
            return False
        return elms[0].__class__.__name__ == 'Head' and elms[1].__class__.__name__ == 'Body'

    def __is_only_title(self, elms) -> bool:
        return elms and len(elms) == 1 and elms[0].__class__.__name__ == 'Title'

    def __is_valid_div(self, elms) -> bool:
        valid_div = {'H1','H2','Div','Table','Ul','Ol','Span','Text','Div'}
        for el in elms:
            if el.__class__.__name__ not in valid_div:
                return False
        return True

    def __is_single_text(self, elms) -> bool:
        return len(elms) == 1 and elms[0].__class__.__name__ == 'Text'

    def __is_only_text(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Text':
                return False
        return True

    def __is_only_ptext(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Text' and el.__class__.__name__ != 'P':
                return False
        return True
    
    def __is_some_li(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Li':
                return False
        return len(elms) >= 1

    def __is_some_thd(self, elms) -> bool:
        if len(elms) == 0:
            return False
        cur = elms[0].__class__.__name__
        if cur != 'Th' and cur != 'Td':
            return False
        for el in elms:
            if el.__class__.__name__ != cur:
                return False
        return True

    def __is_some_tr(self, elms) -> bool:
        for el in elms:
            if el.__class__.__name__ != 'Tr':
                return False
        return True
