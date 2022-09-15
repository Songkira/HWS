from django.urls import path
from . import views

# 앱네임은 템플릿 안에서 url 달때 쓰는 것
app_name = 'articles' # 보통은 앱이름과 동일
urlpatterns = [ 
    # index(예시) : views 안에 있는 함수 이름 
    path('', views.index, name='index'), # articles/로 끝나는 url에 대해서 동작하는 것

    # 게시글 생성/ articles/new/
    path('new/', views.new, name='new'),

    # 게시글 DB에 반영/ articles/create/
    path('create/', views.create, name='create'),

    # 게시글 상세조회 / articles/글번호(pk)/, /articles/2/
    # path converter (컨버터)
    path('<int:pk>/', views.detail, name='detail'), # <str>은 생략가능

    # 게시글 삭제 /  articles/글번호(pk)/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
    
    # 게시글 수정 / articles/글번호(pk)/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 게시글 수정 / articles/글번호(pk)/update/
    path('<int:pk>/update/', views.update, name='update'),
]