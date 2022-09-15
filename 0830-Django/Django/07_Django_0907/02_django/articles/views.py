import re
from tkinter import EW
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import(
    require_http_methods, require_GET, require_POST, require_safe, 
)
from django.contrib.auth.decorators import login_required

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.order_by('-pk') # 최신글 순서대로
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request): # POST 로 돌아감
    # 사용자의 데이터를 받아서
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 유효성 체크를 위해 만듦
        if form.is_valid():
            article = form.save()

            return redirect('articles:detail', article.pk)
        else:
            context = {
                'form': form,
            }
            return render(request, 'articles/create.html', context)
    else: # new 삭제후 코드 그대로 옮겨옴
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk) # if/else 둘다 겹치는 부분은 맨위에
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            # article.save()
            return redirect('articles:detail', article.pk)
    else:
       form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context) 