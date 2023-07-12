from django.db import models

class Review(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASACDE) # 글
    reviewText=models.TextField() #리뷰 댓글
