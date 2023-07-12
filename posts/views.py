from django.shortcuts import render, redirect

from .models import Post

# Create your views here.
def posts_list_view(request): # 전체 글 조회
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list,
    }
    return render(request, 'posts/posts_list.html', context)
