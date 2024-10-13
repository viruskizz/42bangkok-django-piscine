from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies, Planets, People
from .form import MovieSearchForm

# Create your views here.
def index(request):
    try:
        form = MovieSearchForm()
        peoples = []
        if request.method == 'POST':
            form = MovieSearchForm(request.POST)
            date_min = form['date_min'].value()
            date_max = form['date_max'].value()
            diameter = form['diameter'].value()
            gender = form['gender'].value()
            if form.is_valid:
                movies = Movies.objects.filter(release_date__gte=date_min, release_date__lte=date_max).all()
                for m in movies:
                    pp = m.characters.select_related('homeworld').filter(gender=gender, homeworld__diameter__gte=diameter).all()
                    for p in pp:
                        peoples.append({
                            'name': p.name,
                            'gender': p.gender,
                            'homeworld_name': p.homeworld.name if p.homeworld else 'None',
                            'homeworld_diameter': p.homeworld.diameter if p.homeworld else 'None',
                            'movie_title': m.title,
                            'movie_release_date': m.release_date,
                        })
        return render(request, "ex10/index.html", {'form': form, 'peoples': peoples})
    except Exception as e:
        return HttpResponse(e)