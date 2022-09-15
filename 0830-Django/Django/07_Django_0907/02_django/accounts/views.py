from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    # UserCreationForm,
    # UserChangeForm,
    PasswordChangeForm,

) # 1
from django.contrib.auth import login as auth_login # 2
from django.contrib.auth import logout as auth_logout # 3
from .forms import CustomUserCreationForm, CustomUserChangeForm # 4

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
           
    if request.method == 'POST':
        # 두번째의 request.POST 은 첫번째 매개변수에 들어감?
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save() 로그인은 save 필요없음
            auth_login(request, form.get_user())
            # None 이거나 이전 url
            return redirect(request.GET.get('next') or 'articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# POST 요청/ 로그인 사용자만 가능        
def delete(request):
    request.user.delete()  # 로그인 된 사용자에 대한 회원탈퇴
    auth_logout(request) 
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

# 로그인 사용자가 요청해야 합니다.
from django.contrib.auth import update_session_auth_hash
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)# data=request.POST)
        if form.is_valid():
            form.save()
            # 비밀번호 변경하더라도 로그인 상태 유지되도록
            update_session_auth_hash(request, form.user) 
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
