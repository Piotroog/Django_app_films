from django.db import models


class MoreInfo(models.Model):
    TYPE = {
        (0, 'Other'),
        (1, 'Horror'),
        (2, 'Sci-fi'),
        (3, 'Action'),
        (4, 'Romantic'),
        (5, 'Comedy'),
        (6, 'Drama'),
    }
    time = models.PositiveSmallIntegerField(default=0)
    type = models.PositiveSmallIntegerField(default=0, choices=TYPE)
class Film(models.Model):
    title = models.CharField(max_length=64, blank=False)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    bonus = models.OneToOneField(MoreInfo, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title + '(' + str(self.year) + ')'


class Raiting(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    films = models.ManyToManyField(Film)