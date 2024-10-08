from django.http import HttpResponse
from django.shortcuts import render

from django.db import connection

def table_exists(table_name: str) -> bool:
    tables = connection.introspection.table_names()
    print('Tables:', tables)
    return table_name in tables

# to run create new table
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
# 
def init(request):
    # model =
    message = 'OK'
    if not table_exists('ex00_movies'):
        message = 'Error: Table could not created.'
    return HttpResponse(message)