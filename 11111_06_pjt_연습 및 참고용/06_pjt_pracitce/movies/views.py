from django.shortcuts import render, redirect
from .models import Movie, Comment


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
      'movies':movies,
    }
    return render(request, 'movies/index.html', context)

# def index(request):
#     pass
# def index(request):
#     pass
# def index(request):
#     pass
# def index(request):
#     pass
# def index(request):
#     pass