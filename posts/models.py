from django.conf import settings
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="userLike")
    placename=models.CharField('장소명', max_length=50, null=False)
    image=models.ImageField('추천 장소 이미지')
    region=models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    #tag=models.CharField('태그',max_length=50,null=True)
    content=models.TextField('장소에 대한 설명', null=False)
    tip=models.TextField('이렇게 활용하세요!', null=False)
    #theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.placename