from django.urls import path
from . import views # . <- 현재 폴더를 의미

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'), 
    # index는 등록하려 할때 사용
    # index/ 게 들어오면 같은 함수 를 실행
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'),
]