from django.shortcuts import render
from django.http import HttpResponse


def all_films(request):
    return render(request, 'films.html')