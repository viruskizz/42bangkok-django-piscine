# blog/forms.py
from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
import psycopg2
from psycopg2.extras import RealDictCursor

TABLE_NAME = "ex04_movies"

def connect():
    db = "djangotraining"
    username = "djangouser"
    password = "secret"
    conn = psycopg2.connect(f"dbname='{db}' user='{username}' host='127.0.0.1' password='{password}'")
    return conn

def get_all_movies():
    try:
        conn = connect()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cur.fetchall()
        movies = []
        for row in rows:
            movies.append(dict(row))
        conn.commit()
        cur.close()
        conn.close()
        return movies
    except Exception as e:
        print(e)
        return []

# https://forum.djangoproject.com/t/use-form-init-value/24961/2
class MovieListForm(forms.Form):
    title = forms.ChoiceField(
            label='Title')
    class Meta:
        fields = ('title')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        movies = get_all_movies()
        print('init')
        titles = [(m['title'], m['title']) for m in movies]
        self.fields['title'].choices = titles


        