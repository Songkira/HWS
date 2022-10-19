from django.contrib import admin
from .models import Movie, Comment
from atexit import register

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)