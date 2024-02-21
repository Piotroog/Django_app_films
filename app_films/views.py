from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, MoreInfo
from .forms import FilmForm, MoreInfoForm

def all_films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

def new_film(request):
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES)
        more_info_form = MoreInfoForm(request.POST)

        if film_form.is_valid() and more_info_form.is_valid():
            film = film_form.save(commit=False)
            more_info = more_info_form.save()
            film.bonus = more_info
            film.save()
            return redirect(all_films)
    else:
        film_form = FilmForm()
        more_info_form = MoreInfoForm()

    return render(request, 'form_film.html', {'film_form': film_form, 'more_info_form': more_info_form})

def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES, instance=film)
        more_info_form = MoreInfoForm(request.POST, instance=film.bonus)

        if film_form.is_valid() and more_info_form.is_valid():
            film = film_form.save(commit=False)
            more_info = more_info_form.save()
            film.bonus = more_info
            film.save()
            return redirect(all_films)
    else:
        film_form = FilmForm(instance=film)
        more_info_form = MoreInfoForm(instance=film.bonus)

    return render(request, 'form_film.html', {'film_form': film_form, 'more_info_form': more_info_form})

def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm.html', {'film': film})
