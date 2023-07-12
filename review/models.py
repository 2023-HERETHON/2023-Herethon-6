from django.db import models

class Review(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE) # 글
    reviewText=models.TextField() #리뷰 댓글
