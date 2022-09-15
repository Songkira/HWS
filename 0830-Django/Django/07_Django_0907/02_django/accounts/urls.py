from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # /accounts/login
    path('login/', views.login, name='login'),

    # /accounts/logout/
    path('logout/', views.logout , name='logout'),
    
    # /accounts/signup/ 회원가입
    path('signup/', views.signup, name='signup'),

    # /accounts/delete/ 회원탈퇴
    path('delete/', views.delete, name='delete'),

    # /accounts/update/ 회원정보 수정
    path('update/', views.update, name='update'),

    # /accounts/password/ 비밀번호 변경
    path('password/', views.change_password, name='change_password'),
]
