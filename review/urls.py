from django.urls import path
from .views import review_list

app_name = "review"

urlpatterns = [
    #path('', review_view2),
    path('<int:post_id>/', review_list, name="review-view")
]