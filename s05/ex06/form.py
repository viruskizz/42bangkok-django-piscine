# blog/forms.py
from django import forms
import psycopg2
from psycopg2.extras import RealDictCursor

# TABLE_NAME = "ex04_movies"

# def connect():
#     db = "djangotraining"
#     username = "djangouser"
#     password = "secret"
#     conn = psycopg2.connect(f"dbname='{db}' user='{username}' host='127.0.0.1' password='{password}'")
#     return conn

from . import connect, exec_commands, TABLE_NAME

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
        label='Title',
        widget=forms.Select(attrs={'class': 'form-control mb-2'})    
    )
    class Meta:
        fields = ('title')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        movies = get_all_movies()
        titles = [(m['title'], m['title']) for m in movies]
        self.fields['title'].choices = titles

class MovieUpdateForm(forms.Form):
    title = forms.ChoiceField(
        label='Title',
        widget=forms.Select(attrs={'class': 'form-control mb-2'})    
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )

    class Meta:
        fields = ('title', 'description')
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        movies = get_all_movies()
        titles = [(m['title'], m['title']) for m in movies]
        self.fields['title'].choices = titles