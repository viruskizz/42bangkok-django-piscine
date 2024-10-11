from django import forms
from .models import Movies

class MovieListForm(forms.Form):
    title = forms.ChoiceField(
        label='Title',
        widget=forms.Select(attrs={'class': 'form-control mb-2'})    
    )
    class Meta:
        fields = ('title')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        movies = list(Movies.objects.all().values())
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
        movies = list(Movies.objects.all().values())
        titles = [(m['title'], m['title']) for m in movies]
        self.fields['title'].choices = titles