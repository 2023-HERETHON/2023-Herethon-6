
from django.shortcuts import render, redirect

from django.contrib import auth
from .forms import UserForm
from django.contrib.auth import authenticate, login
from posts.models import Post
from review.models import Review
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request): # 로그인
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse('main2')) # 성공
            return HttpResponseRedirect(reverse('user:user-main2')) # 성공
        else:
            return render(request, 'user/login.html') #실패


def signup_view(request): # 회원가입
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            #return redirect('main2')
            return redirect('user:user-main2')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})

def main1(request): # 로그인 전 페이지
    return render(request, 'main1.html')

def consulting_view(request): # 컨설팅 페이지
    if request.method == 'POST':
        return render(request, 'user/consulting.html')


def main2(request): # 로그인 후  페이지
    return render(request, 'user/main2.html')


def logout_view(request):
    return

# def like_list_view(request, pk):
#     if request.method == 'GET':
#         likeList = posts.models.Post.objects.filter(like=pk)
#         context = {
#             'likeList': likeList,
#         }
#         return render(request, 'user/saveList.html', context)
def like_list_view(request, id): # 마이페이지 찜 목록 보기
    likeList = Post.objects.filter(like=request.user.id)
    context = {
        'likeList': likeList,
    }
    return render(request, 'user/saveList.html', context)

def review_list_view(request, id): # 마이페이지 리뷰 목록 보기
    reviewList = Review.objects.filter(user=request.user.id)
    context = {
        'reviewList': reviewList,
    }
    return render(request, 'user/myPage.html', context)