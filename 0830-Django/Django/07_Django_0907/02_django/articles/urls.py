from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # 게시글 생성
    # path('new/', views.new, name='new'), # new 삭제 -> 하나로 합치기위해
    path('create/', views.create, name='create'),

    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 게시글 수정
    # edit 삭제 -> 하나로 합치기위해
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
