from django.contrib import admin
from .models import Film, MoreInfo, Raiting

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "imdb_rating", "year"]

admin.site.register(MoreInfo)
admin.site.register(Raiting)