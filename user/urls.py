from django.urls import path
from .views import login_view, signup_view, logout_view, like_list_view

app_name = "user"

urlpatterns = [
    path("login/", login_view, name='user-login'),
    path("signup/", signup_view, name='user-signup'),
    path("logout/", logout_view, name='user-logout'),
    path('<int:id>/like/', like_list_view, name='user-like'),
]