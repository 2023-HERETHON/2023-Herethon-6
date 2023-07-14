from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Tag, Region, Category
from urllib.parse import urlencode

from review.models import Review


# Create your views here.
def posts_list_view(request):  # 전체 글 조회
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list,
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail_view(request, id):  # 세부 글 조회
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'posts/posts_detail.html', context)


def posts_like_view(request, id):  # 찜
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    if request.method == 'POST':
        if post.like.filter(id=request.user.id).exists():  # 찜 이미 누른 상태일 때
            post.like.remove(request.user)  # 찜 취소
            post.save()
        else:  # 찜  누르지 않은 상태일 때
            post.like.add(request.user)  # 찜 등록
            post.save()
        return render(request, 'posts/posts_detail.html', context)
def filter_posts(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        tags = Tag.objects.all()
        categories = Category.objects.all()
        return render(request, 'posts/filter.html', {'regions': regions, 'tags': tags, 'categories': categories})
    else:
        return render(request, 'posts/filter.html')

def filtered_posts(request):
    if request.method == 'GET':
        tag_ids = request.GET.getlist('tag')
        region_id = request.GET.get('region')
        category_id = request.GET.get('category')

        selected_tags = Tag.objects.filter(id__in=tag_ids)
        selected_region = Region.objects.get(id=region_id)

        posts = Post.objects.filter(region=selected_region)
        if selected_tags:
            for tag in selected_tags:
                posts = posts.filter(tags=tag)

        if category_id:
            category = Category.objects.get(id=category_id)
            posts = posts.filter(categories=category)

        categories = Category.objects.all()

        query_dict = {'tag': tag_ids, 'region': region_id}
        query_string = urlencode(query_dict, doseq=True)

        return render(request, 'posts/filtered_post.html',
                      {'posts': posts, 'categories': categories, 'query_string': query_string})

def review_create_view(request, id): # 리뷰 생성
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        return render(request, 'posts/review_form.html')
    else:
        reviewTitle = request.POST.get('reviewTitle')
        reviewText = request.POST.get('reviewText')
        user = request.user
        rating=request.POST.get('rating') #별점 값 가져오기

        Review.objects.create(
            post=post,
            reviewTitle=reviewTitle,
            reviewText=reviewText,
            user=user,
            rating=rating
        )
        return redirect('posts:post-detail', id=post.id)


def review_delete_view(request,id): # 리뷰 삭제
    #post = get_object_or_404(Post, id=id)

    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        review.delete()
        return redirect(f"/user/{request.user.id}/review/")


def review_edit_view(request, id): # 리뷰 수정
    review = get_object_or_404(Review, id=id)

    if request.method == 'GET':
        context = { 'review' : review }
        return render(request,'posts/review_form.html', context)
    elif request.method == 'POST':
        reviewTitle = request.POST.get('reviewTitle')
        reviewText = request.POST.get('reviewText')
        # 데이터 변경(수정)
        review.reviewTitle = reviewTitle
        review.reviewText = reviewText
        review.save()

        return redirect(f"/user/{request.user.id}/review/")

# def create_review(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.post = post
#             review.user = request.user
#             review.save()
#             return redirect('http://127.0.0.1:8000/posts/1/review/')
#     else:
#         form = ReviewForm()
#
#     context = {
#         'form': form,
#         'post_id': post_id,
#     }
#     return render(request, 'posts/create_review.html', context)




