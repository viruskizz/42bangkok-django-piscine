from elem import Elem

def create_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

if __name__ == '__main__':
    doc = Elem(name="!DOCTYPE html", is_simple=True)
    html = Elem(name="html", attrs={"lang": "en"})
    head = Elem(name="head")
    meta1 = Elem(name="meta", is_simple=True, attrs={'charset': 'UTF-8'})
    meta2 = Elem(name="meta", is_simple=True, attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'})
    title = Elem(name="title")
    title.add_content("element")
    head.add_content(meta1, meta2, title)
    html.add_content(head)
    doc.add_content(html, is_after=True)
    print(doc)
    create_file("test.html", str(doc))