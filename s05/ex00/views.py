from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

# to run create new table
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver
# 
def init(request):
    message = "OK"
    db = "djangotraining"
    username = "djangouser"
    password = "secret"
    try:
        conn = psycopg2.connect(f"dbname='{db}' user='{username}' host='127.0.0.1' password='{password}'")
        cur = conn.cursor() 
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title varchar(64) NOT NULL UNIQUE,
                episode_nb serial PRIMARY KEY,
                opening_crawl text,
                director varchar(32) NOT NULL,
                producer varchar(128) NOT NULL,
                release_date date NOT NULL
            )
            """
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)
        message = e
    return HttpResponse(message)