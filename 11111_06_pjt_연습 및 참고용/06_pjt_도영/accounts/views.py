from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from . forms import CustomUserCreatopmForm, CustomUserChangeForm
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.

# 로그인
# 겟 포스트
@require_http_methods(['POST', 'GET'])
def login(request):
    # if request.user.is_authenticated:
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
# 포스트
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

# 회원가입
# 겟 포스트
@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreatopmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserCreatopmForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

# 회원정보 수정
# 겟 포스트
@require_http_methods(['POST', 'GET'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_vali():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)

# 회원 탈퇴
# 포스트
@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')

# 비밀번호 변경
# 겟 포스트
@require_http_methods(['POST', 'GET'])
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/password_change.html', context)
