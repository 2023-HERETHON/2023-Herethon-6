from django.urls import path
from .views import posts_list_view, posts_detail_view, posts_like_view

app_name = "posts"

urlpatterns = [
    path("list/", posts_list_view, name='post-list'),
    path("<int:id>/", posts_detail_view, name='post-detail'),
    path('<int:id>/like/', posts_like_view, name='post-like'),
]

