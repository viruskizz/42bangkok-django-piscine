from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    message = "Hello World"
    # return render(request, )