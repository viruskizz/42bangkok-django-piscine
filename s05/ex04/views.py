from django.http import HttpResponse
from django.shortcuts import render

from .models import MovieModel
from .form import MovieListForm

# Create your views here.
def init(request):
    try:
        MovieModel().setup()
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
        results = MovieModel().bulk_insert(data)
        return render(request, "ex04/populate.html", {"results": results})
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        movies = MovieModel().list()
        return render(request, "ex04/display.html", {"movies": movies})
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
        return render(request, "ex04/remove.html", {"form": form, "moviesCount": moviesCount ,"record": selected})
    except Exception as e:
        return HttpResponse(e)
