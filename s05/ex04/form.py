# blog/forms.py
from django import forms
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

class MovieListForm(forms.Form):
    movies = get_all_movies()
    titles = [m['title'] for m in movies]
    title = forms.CharField(
        label='Title',
        widget=forms.Select(
            choices=[(k, k) for k in titles],
            attrs={'class': 'form-control my-2'})
    )