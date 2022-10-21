from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length = 100)

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name = 'movie_actors', through = 'Movies_acotrs')

class Review(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

class Movies_acotrs(models.Model):
    movies = models.ForeignKey(Movie, on_delete = models.CASCADE)
    actors = models.ForeignKey(Actor, on_delete = models.CASCADE)

