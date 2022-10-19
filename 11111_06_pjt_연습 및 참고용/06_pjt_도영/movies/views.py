from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Comment, Movie
from .forms import CommentForm, MovieForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments':comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['POST','GET'])
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

# @require_POST
# def delete(request,movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     movie.delete()
#     return redirect('movies:index')

@require_POST
def delete(request,movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if request.user == movie.user:
            movie.delete()
    return redirect('movies:index')


# 데코레이터
@require_POST
def comments_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.movie = movie
    #         comment.save()
    #     return redirect('movies:detail', movie.pk)
    # else:
    #     comment_form = CommentForm()
    # context = {
    #     'comment_form' : comment_form
    # }
    # return render()

@require_POST
def comments_delete(request, movie_pk, comment_pk ):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('movies:detail', movie_pk)