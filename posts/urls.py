from django.urls import path
from .views import posts_list_view

app_name = "posts"

urlpatterns = [
    path("list/", posts_list_view, name='post-list'),
]
