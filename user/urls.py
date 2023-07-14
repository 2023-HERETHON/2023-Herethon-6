from django.urls import path
#from .views import login_view, signup_view, logout_view, like_list_view
from .views import login_view, signup_view, logout_view, like_list_view, main2, review_list_view

app_name = "user"

urlpatterns = [
    path("login/", login_view, name='user-login'),
    path("main2/", main2, name='user-main2'),
    # path("consulting/", consulting_view, name='user-consulting'),
    path("signup/", signup_view, name='user-signup'),
    path("logout/", logout_view, name='user-logout'),
    path('<int:id>/like/', like_list_view, name='user-like'),
    path('<int:id>/review/', review_list_view, name='user-review'),
]