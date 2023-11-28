from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
def all_films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'form_film.html', {'form': form})

def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(all_films)

    return render(request, 'form_film.html', {'form': form})

def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_films)



    return render(request, 'confirm.html', {'film': film})