from django.shortcuts import render
from django.http import HttpResponse

from .form import MovieListForm

from .models import Movies

data = [
    {'episode_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
    {'episode_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
    {'episode_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
    {'episode_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
    {'episode_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1980-05-17'},
    {'episode_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand', 'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
    {'episode_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
]
# Create your views here.
def populate(request):
    try:
        for d in data:
            movie = Movies(**d)
            movie.save()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def display(request):
    try:
        movies = list(Movies.objects.all().values())
        return render(request, "ex05/display.html", {"movies": movies})
    except Exception as e:
        return HttpResponse(e)
    
def remove(request):
    try:
        selected = ""
        moviesCount = Movies.objects.count()
        form = MovieListForm()
        if request.method == "POST":
            form = MovieListForm(request.POST)
            title = form['title'].value()
            record = Movies.objects.filter(title=title)
            selected = Movies.objects.get(title=title)
            if form.is_valid():
                record.delete()
                moviesCount -= 1
                form = MovieListForm()
        return render(request, "ex05/remove.html", {"form": form, "moviesCount": moviesCount, "selected": selected})
    except Exception as e:
        return HttpResponse(e)
