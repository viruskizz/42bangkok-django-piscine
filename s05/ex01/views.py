from django.http import HttpResponse
from django.shortcuts import render

from django.db import connection

def table_exists(table_name: str) -> bool:
    tables = connection.introspection.table_names()
    print('Tables:', tables)
    return table_name in tables

def index(request):
    message = 'OK'
    if not table_exists('ex01_movies'):
        message = 'Error: Table could not created.'
    return HttpResponse(message)