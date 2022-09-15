"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# articles앱 ->view.py 를 import
# from articles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # include에 작성한 안에있는 url을 찾아서 
    path('articles/', include('articles.urls')), # 앱이름.urls
    path('pages/', include('pages.urls')),
    # path('index/', views.index), 
    # # index는 등록하려 할때 사용
    # # index/ 게 들어오면 같은 함수 를 실행
    # path('greeting/', views.greeting),
    # path('dinner/', views.dinner),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<str:name>/<int:age>', views.hello),
    # <:name>으로 들어가느 것은 views 에서 def hello(request, name): 중 name
]
