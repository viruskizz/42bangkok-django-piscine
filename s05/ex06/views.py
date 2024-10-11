from django.http import HttpResponse
from django.shortcuts import render

from .models import MovieModel
from . import connect, exec_commands, TABLE_NAME
from .form import MovieListForm, MovieUpdateForm

# Create your views here.
def init(request):
    try:
        exec_commands([
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                title VARCHAR(64) NOT NULL UNIQUE,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL,
                updated TIMESTAMP NOT NULL
            )
            """,
            ## Add created field before insert record
            f"""
            CREATE OR REPLACE FUNCTION create_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.created = now();
                NEW.updated = now();
                RETURN NEW;
            END
            $$ language 'plpgsql';
            CREATE TRIGGER create_changetimestamp_column BEFORE INSERT
            ON {TABLE_NAME} FOR EACH ROW EXECUTE PROCEDURE
            create_changetimestamp_column();
            """,
            ## Add updated field before update record
            f"""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON {TABLE_NAME} FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """
        ])
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def populate(request):
    data = [
        {'episode_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
        {'episode_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
        {'episode_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
        {'episode_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
        {'episode_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1980-05-17'},
        {'episode_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand', 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
        {'episode_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
    ]
    try:
        MovieModel().bulk_insert(data)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        movies = MovieModel().list()
        return render(request, "ex06/display.html", {"movies": movies})
    except Exception as e:
        return HttpResponse(e)

def remove(request):
    try:
        form = MovieListForm()
        moviesCount = len(MovieModel().list())
        selected = ""
        if request.method == "POST":
            form = MovieListForm(request.POST)
            title = form['title'].value()
            selected = MovieModel().get({'title': title})
            if form.is_valid():
                model = MovieModel()
                model.remove({'title': title})
                moviesCount -= 1
                form = MovieListForm()
        return render(request, "ex06/remove.html", {"form": form, "moviesCount": moviesCount ,"record": selected})
    except Exception as e:
        return HttpResponse(e)

def update(request):
    try:
        form = MovieUpdateForm()
        moviesCount = len(MovieModel().list())
        if request.method == "POST":
            form = MovieUpdateForm(request.POST)
            model = MovieModel()
            title = form['title'].value()
            description = form['description'].value()
            if form.is_valid():
                form = MovieUpdateForm()
                model.update({'title': title}, {'opening_crawl': description})
        return render(request, "ex06/update.html", {"form": form, "moviesCount": moviesCount })
    except Exception as e:
        return HttpResponse(e)