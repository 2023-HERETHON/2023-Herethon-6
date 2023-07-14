# from django.urls import path
# from .views import posts_list_view, posts_detail_view, posts_like_view
# from . import views
#
# app_name = "posts"
#
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('', views.filter_posts, name='filter_posts'),
#     # path('filter/', views.filtered_posts, name='filtered_posts'),
#     path('filter/<int:category>/', views.filtered_posts, name='filtered_posts'),
#     path("list/", posts_list_view, name='post-list'),
#     path("<int:id>/", posts_detail_view, name='post-detail'),
#     path('<int:id>/like/', posts_like_view, name='post-like'),
# ]

from review.views import review_list
from django.urls import path
from .views import posts_list_view, posts_detail_view, posts_like_view, filter_posts, filtered_posts, review_create_view, review_delete_view, review_edit_view
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.filter_posts, name='filter_posts'),
    path('filter/', views.filtered_posts, name='filtered_posts'),
    path('list/', posts_list_view, name='post-list'),
    path('<int:id>/', posts_detail_view, name='post-detail'),
    path('<int:id>/like/', posts_like_view, name='post-like'),
    #path('filter/<int:category>/', views.filtered_posts, name='filtered_posts'),
    path('<int:post_id>/review/', review_list, name="review-view"),
    #path('<int:post_id>/review/create/', views.create_review, name='create_review'),
    path('<int:id>/review/create/', views.review_create_view, name='create_review'),
    path('<int:id>/review/delete/', review_delete_view, name='review-delete'),
    path('<int:id>/review/edit/', review_edit_view, name='review-edit'),
]
