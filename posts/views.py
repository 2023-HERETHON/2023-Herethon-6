from django.shortcuts import render, redirect, get_object_or_404

from .models import Post

# Create your views here.
def posts_list_view(request): # 전체 글 조회
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list,
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail_view(request, id): # 세부 글 조회
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'posts/posts_detail.html', context)