from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('init', views.init, name="init"),
    path('populate', views.populate, name="populate"),
    path('display', views.display, name="display"),
    path('remove', views.remove, name="remove"),
]
