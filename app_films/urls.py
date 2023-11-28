from django.urls import path
from app_films.views import all_films, new_film, edit_film

urlpatterns = [
    path('all_films/', all_films),
    path('new/', new_film),
    path('edit/<int:id>/', edit_film),
]
