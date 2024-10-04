from Page import *

if __name__ == '__main__':
    # try:
        html = Html([
            Head([
                Title([
                      Text('This is Title')
                ]),
            ]),
            Body([
                H1([
                      Text('"Oh no, not again!"')
                ]),
                # Img(attrs={'src': 'http://i.imgur.com/pfp3T.jpg'}),
                Div([
                    Div([
                          Span([
                                P([
                                    #   Div()
                                    Text()
                                ]),
                                Text()
                                # Div()
                          ])
                    ]),
                    # Title()
                    Table([
                        Tr([
                            Th([
                                Text("Table Tr Th")
                            ])
                        ])
                    ])
                ]),
                Ol([
                    Li([
                          Text("Li Hello, world!")
                    ]),
                    #   Li(),
                    #   Li(),
                    #   Div()
                ])
            ]),
        ])
        page = Page(html)
        valid = page.is_valid()
        print(valid)
        print(page)
        print(Page([Head(), Body()]).is_valid())
        page.write_to_file("index.html")
        print("True:", Page(Html([Head(Title(Text('title'))), Body()])).is_valid())