from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Tag, Region, Category


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

# def home(request):
#     tags = Tag.objects.all()
#     regions = Region.objects.all()
#     return render(request, 'posts/filter.html',{'tags': tags, 'regions': regions})

# def filter_posts(request):
#     if request.method == 'POST':
#         tag_ids = request.POST.getlist('tag')
#         region_id = request.POST.get('region')
#         selected_tags = Tag.objects.filter(id__in=tag_ids)
#         selected_region = Region.objects.get(id=region_id)
#
#         posts = Post.objects.filter(region=selected_region)
#         for tag in selected_tags:
#             posts = posts.filter(tags=tag)
#
#         regions = Region.objects.all()
#         tags = Tag.objects.all()
#
#         return render(request, 'posts/filtered_post.html', {'posts': posts, 'regions': regions, 'tags': tags})
#     regions = Region.objects.all()
#     tags = Tag.objects.all()
#     return render(request, 'posts/filter.html', {'regions': regions, 'tags': tags})

def filter_posts(request):
    if request.method == 'POST':
        tag_ids = request.POST.getlist('tag')
        region_id = request.POST.get('region')
        selected_tags = Tag.objects.filter(id__in=tag_ids)
        selected_region = Region.objects.get(id=region_id)

        posts = Post.objects.filter(region=selected_region)
        for tag in selected_tags:
            posts = posts.filter(tags=tag)

        regions = Region.objects.all()
        tags = Tag.objects.all()
        categories = Category.objects.all()

        return render(request, 'posts/filtered_post.html',
                      {'posts': posts, 'regions': regions, 'tags': tags, 'categories': categories})

    regions = Region.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'posts/filter.html', {'regions': regions, 'tags': tags, 'categories': categories})


def filtered_posts(request):
    category_id = request.GET.get('category')
    category = Category.objects.get(id=category_id)
    # posts = Post.objects.filter(category=category)
    tags_in_category = Tag.objects.filter(tags__category=category)

    posts = Post.objects.filter(tags__in=tags_in_category)

    regions = Region.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()

    return render(request, 'posts/filtered_post.html',
                  {'posts': posts, 'regions': regions, 'tags': tags, 'categories': categories, 'category': category})

# def filter_posts(request):
#     if request.method == 'POST':
#         tag_ids = request.POST.getlist('tag')
#         region_id = request.POST.get('region')
#         selected_tags = Tag.objects.filter(id__in=tag_ids)
#         selected_region = Region.objects.get(id=region_id)
#
#         posts = Post.objects.filter(region=selected_region)
#         for tag in selected_tags:
#             posts = posts.filter(tags=tag)
#
#         regions = Region.objects.all()
#         tags = Tag.objects.all()
#         categories = Category.objects.all()
#
#         return render(request, 'posts/filtered_post.html', {
#             'posts': posts,
#             'regions': regions,
#             'tags': tags,
#             'categories': categories,
#             'selected_tags': selected_tags,
#             'selected_region': selected_region
#         })
#
#     regions = Region.objects.all()
#     tags = Tag.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'posts/filter.html', {
#         'regions': regions,
#         'tags': tags,
#         'categories': categories
#     })
#
#
# def filtered_posts(request, category):
#     category = get_object_or_404(Category, id=category)
#     tags_in_category = Tag.objects.filter(category=category)
#
#     posts = Post.objects.filter(region=request.GET.get('region'), tags__in=tags_in_category)
#
#     regions = Region.objects.all()
#     tags = Tag.objects.all()
#     categories = Category.objects.all()
#
#     return render(request, 'posts/filtered_post.html', {
#         'posts': posts,
#         'regions': regions,
#         'tags': tags,
#         'categories': categories,
#         'category': category
#     })






