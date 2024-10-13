# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import PeopleModel, PlanetModel

# Create your views here.
def init(request):
    try:
        PlanetModel().setup()
        PeopleModel().setup()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def populate(request):
    try:
        PlanetModel().bulk_from_file(
            "static/ex08/planets.csv",
            ['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain']
        )
        PeopleModel().bulk_from_file(
            "static/ex08/people.csv",
            ['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld']
        )
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        peoples = PeopleModel().list()
        return render(request, "ex08/display.html", {"peoples": peoples})
    except Exception as e:
        return HttpResponse(e)
