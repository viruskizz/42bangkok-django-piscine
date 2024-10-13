from django import forms
from .models import Movies, People
from django.db.models import Max, Min

class MovieSearchForm(forms.Form):
    date_min = forms.DateField(label='Date Maximum')
    date_max = forms.DateField(label='Date Maximum')
    diameter = forms.IntegerField(
        label='Planet Diameter',
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'input numbers'})
    )
    gender = forms.ChoiceField(
        label='Gender',
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )

    class Meta:
        fields = ('date_min', 'date_max', 'diameter', 'gender')
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        people_dist = People.objects.distinct('gender').values()
        movies_min = Movies.objects.aggregate(Min('release_date')).values()
        movies_max = Movies.objects.aggregate(Max('release_date')).values()
        genders = [(p['gender'], p['gender']) for p in list(people_dist)]
        # Setup Form 
        self.fields['gender'].choices = genders
        date_min = list(movies_min)[0]
        date_max = list(movies_max)[0]
        self.fields['date_min'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': date_min,
                'max': date_max,
            }
        )
        self.fields['date_max'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': date_min,
                'max': date_max,
            }
        )