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


def posts_like_view(request, id): #찜
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        if post.like.filter(id=request.user.id).exists(): # 찜 이미 누른 상태일 때
            post.like.remove(request.user) # 찜 취소
            post.save()
        else: # 찜  누르지 않은 상태일 때
            post.like.add(request.user) # 찜 등록
            post.save()
        return redirect('posts:post-list')