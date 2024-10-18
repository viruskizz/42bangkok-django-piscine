from django.http import HttpResponse
from django.shortcuts import render

from .models import People

# Create your views here.
def init(request):
    try:
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        peoples = People.objects.filter(homeworld__climate__contains = 'windy').order_by('name')
        return render(request, "ex09/display.html", {"peoples": peoples})
    except Exception as e:
        return HttpResponse(e)
