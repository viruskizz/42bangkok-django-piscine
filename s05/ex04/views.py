from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import psycopg2
from psycopg2.extras import RealDictCursor
from django.urls import reverse

from .form import MovieListForm

TABLE_NAME = "ex04_movies"

def connect():
    db = "djangotraining"
    username = "djangouser"
    password = "secret"
    conn = psycopg2.connect(f"dbname='{db}' user='{username}' host='127.0.0.1' password='{password}'")
    return conn

# Create your views here.
def init(request):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                title varchar(64) NOT NULL UNIQUE,
                episode_nb serial PRIMARY KEY,
                opening_crawl text,
                director varchar(32) NOT NULL,
                producer varchar(128) NOT NULL,
                release_date date NOT NULL
            )
            """)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def populate(request):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"""
            INSERT INTO {TABLE_NAME} (episode_nb, title, director, producer, release_date) 
            VALUES
                (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
                (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
                (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
                (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
                (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
                (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
                (7, 'The Force Awakens', 'J. J. Abrams', ' Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
            """)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE_NAME}")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render(request, "ex04/display.html", {"rows": rows})
    except Exception as e:
        return render(request, "ex04/display.html", {"rows": []})

def remove(request, context={}):
    form = MovieListForm()
    if request.method == "POST":
        form = MovieListForm(request.POST)
        title = form['title'].value()
        conn = connect()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE \"title\" = '{title}' limit 1")
        row = cur.fetchone()
        print(row)
        selected = dict(row) if row else ""
        cur.execute(f"DELETE FROM {TABLE_NAME} WHERE \"title\" = '{title}'")
        conn.commit()
        cur.close()
        conn.close()
        print(selected)
        if form.is_valid():
            newform = MovieListForm()
            return render(request, "ex04/remove.html", {"form": newform,"record": selected})
    return render(request, "ex04/remove.html", {"form": form, "record": ""})
