from django.shortcuts import render
from .models import Film
from .forms import FilmForm
def all_films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    return render(request, 'new_film.html', {'form': form})