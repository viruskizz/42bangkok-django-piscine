from django.shortcuts import render

# Create your views here.
def index(request):
    shades = []
    for c in [x * 5.2 for x in range(50)]:
        cc = 255 - round(c)
        shades.append({
            'r': f'background-color: rgb({cc}, 0, 0)',
            'g': f'background-color: rgb(0, {cc}, 0)',
            'b': f'background-color: rgb(0, 0, {cc})',
            'a': f'background-color: rgb({cc}, {cc}, {cc})',
        })
    return render(request, "ex03/index.html", {"shades": shades})