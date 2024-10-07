from django.shortcuts import render
from datetime import datetime

# Create your views here.
def django(request):
    context = {}
    return render(request, 'django.html', context)

def display(request):
    context = {}
    return render(request, 'display.html', context)

def templates(request):
    context = {
        'title': 'Django Template Engine',
        'code_var': """<img src="{% static imgUrl %}" width="720" alt="My image">""",
        'code_for': """
<ul>
    {% for serie in series %}
        <li>{{serie}}</li>
    {% endfor %}
</ul>""",
"code_if": """
{% if timer.second|divisibleby:2 %}
    <p><b style="color: green">{{timer.isoformat}}</b></p>
{% else %}
    <p><b style="color: red">{{timer.isoformat}}</b></p>
{% endif %}""",
        'timer': datetime.now(),
        'series': [
            'Final Fantasy V',
            'Final Fantasy VII',
            'Final Fantasy IX',
            'Final Fantasy XIV',
            'Final Fantasy XV',
        ],
        'imgUrl': 'images/example.png'
    }
    return render(request, 'templates.html', context)