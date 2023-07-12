from django.db import models

# Create your models here.
class Post(models.Model):

    placename=models.CharField('장소명', max_length=50, null=False)
    image=models.ImageField('추천 장소 이미지')
    region=models.CharField('구', max_length=20, null=True)
    tag=models.CharField('태그',max_length=50,null=True)
    content=models.TextField('장소에 대한 설명', null=False)
    tip=models.TextField('이렇게 활용하세요!', null=False)