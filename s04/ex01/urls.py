from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('django/', views.django, name="index"),
    path('display/', views.display, name="index"),
    path('templates/', views.templates, name="index")
]
