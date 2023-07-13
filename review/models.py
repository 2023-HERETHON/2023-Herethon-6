from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE) # 글
    reviewText=models.TextField() #리뷰 댓글
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # User와의 Foreign Key