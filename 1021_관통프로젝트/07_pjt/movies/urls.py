from django.urls import path
from . import views

urlpatterns = [
    # 배우 전체 조회
    path('actor/', views.actor_list),
    # 배우 상세 조회
    path('actor/<int:actor_pk>/', views.actor_detail),
    # 영화 전체 조회
    path('movie/', views.movie_list),
    # 영화 상세 조회
    path('movie/<int:movie_pk>/', views.movie_detail),
    # 리뷰 전체 조회
    path('review/', views.review_list),
    # 리뷰 상세 조회
    path('review/<int:review_pk>/', views.review_detail),
    # 리뷰 생성
    path('movie/<int:movie_pk>/review_create/', views.review_create),
]
