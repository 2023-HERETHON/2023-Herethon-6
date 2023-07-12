from django.shortcuts import render, redirect

from django.contrib import auth
from .forms import UserForm
from django.contrib.auth import authenticate, login

def login_view(request):

    return


def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main2')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})

def main2(request): # home 페이지
    return render(request, 'main2.html')

def logout_view(request):
    return


