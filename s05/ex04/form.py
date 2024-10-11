# blog/forms.py
from django import forms
from .models import MovieModel

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
        movies = MovieModel().list()
        titles = [(m['title'], m['title']) for m in movies]
        self.fields['title'].choices = titles