from django.shortcuts import render

# Create your views here.
def django(request):
    context = {}
    return render(request, 'django.html', context)

def display(request):
    context = {}
    return render(request, 'display.html', context)

def templates(request):
    context = {}
    return render(request, 'templates.html', context)