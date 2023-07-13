from django.conf import settings
from django.db import models
from posts.models import Post


class Review(models.Model):
    #post = models.ForeignKey('posts.Post', on_delete=models.CASCADE) # 글
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reviewTitle = models.TextField(max_length=50, default="제목 없음")  # 리뷰 제목
    reviewText = models.TextField() #리뷰 댓글
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # User와의 Foreign Key