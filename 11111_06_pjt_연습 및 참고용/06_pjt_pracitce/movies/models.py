from django.db import models
from accounts.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    uesr = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)