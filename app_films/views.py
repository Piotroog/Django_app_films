from django.shortcuts import render
from .models import Film

def all_films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})
