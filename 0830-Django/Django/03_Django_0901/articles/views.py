from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 쿼리셋 리스트 값을 넘겨줌
    # articles = Article.objects.all()
    # articles = Article.objects.all()[::-1] # 오름차순
    # articles = Article.objects.order_by('pk') # 오름차순
    articles = Article.objects.order_by('-pk') # 내림차순
    context = {
        'articles': articles,
    }
    # 'index.html' = 템플릿
    # ret = render(request, 'index.html', context)
    # return ret
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    # return render(request, 'articles/index.html')
    # render : 가지고 있는 걸 보여주는건
    # redirect: create 받아서 인덱스 번호로 다시 돌려주는 느낌?
    return redirect('articles:detail', article.pk) # /articles/


# /articles/<int:pk>/
def detail(request, pk):
    article = Article.objects.get(pk=pk) # 조회
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
        
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    
    article.save()
    return redirect('articles:detail', article.pk)    
    