from elements import *

def create_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

if __name__ == '__main__':
    doc = Html([
        Head([
            Title().add_content('"Hello ground!"')
        ]),
        Body([
            H1().add_content('"Oh no, not again!"'),
            Img(attrs={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(doc)
    create_file("test.html", str(doc))
