from django.contrib import admin
from django.urls import include, path
from . import view

urlpatterns = [
    path('', view.index, name="index")
]
