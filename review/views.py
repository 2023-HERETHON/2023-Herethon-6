from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from .models import Review

#def review_view2(request): # 상세페이지조회 잠시!
    #return render(request, 'detail.html')


def review_list(request, post_id):
    reviews = Review.objects.filter(post_id=post_id)  # post_id에 해당하는 리뷰들 가져오기
    return render(request, 'reviewall.html', {'reviews': reviews})