from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('init', views.init, name="populate"),
    path('populate', views.populate, name="populate"),
    path('display', views.display, name="display"),
]
