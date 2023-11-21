from django.urls import path
from app_films.views import all_films

urlpatterns = [
    path('all_films', all_films),
]
