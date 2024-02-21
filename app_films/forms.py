from django.forms import ModelForm
from .models import Film, MoreInfo

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'description', 'premiere', 'imdb_rating', 'poster', 'bonus']
        exclude = ['bonus']

class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['time', 'type']