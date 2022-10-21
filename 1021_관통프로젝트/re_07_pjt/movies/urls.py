from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('review/', views.review_list),
    path('review/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/review/', views.review_create),
]
