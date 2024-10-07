from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    context = {
        'name': 'Araiva',
        'tags': {
            'overview': {
                'description': 'Nearly all Markdown applications support the basic syntax outlined in the original Markdown design document. There are minor variations and discrepancies between Markdown processors — those are noted inline wherever possible.'
            },
            'headings': {
                'description': 'To create a heading, add number signs (#) in front of a word or phrase. The number of number signs you use should correspond to the heading level. For example, to create a heading level three (<h3>), use three number signs (e.g., ### My Header).',
                'details': [
                    {
                        'title': '# Heading level 1',
                        'example': '<h1>Heading level 1</h1>',
                    },
                    {
                        'title': '# Heading level 2',
                        'example': '<h1>Heading level 2</h1>',
                    },
                    {
                        'title': '# Heading level 3',
                        'example': '<h1>Heading level 3</h1>',
                    },
                    {
                        'title': '# Heading level 3',
                        'example': '<h1>Heading level 3</h1>',
                    },
                    {
                        'title': '# Heading level 4',
                        'example': '<h1>Heading level 4</h1>',
                    },
                    {
                        'title': '# Heading level 5',
                        'example': '<h1>Heading level 5</h1>',
                    },
                    {
                        'title': '# Heading level 6',
                        'example': '<h1>Heading level 6</h1>',
                    },
                ]
            },
            'alternative syntax': {
                'description': 'Alternatively, on the line below the text, add any number of == characters for heading level 1 or -- characters for heading level 2.',
                'details': [
                    {
                        'title': 'Heading level 1 </br>===============',
                        'example': '<h1>Heading level 1</h1>',
                    },
                    {
                        'title': 'Heading level 2 </br>===============',
                        'example': '<h1>Heading level 2</h1>',
                    }
                ]
            }
        }
    }
    return render(request, 'ex00/index.html', context)