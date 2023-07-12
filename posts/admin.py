from django.contrib import admin
from .models import Post # Post 클래스를 사용하기 위해 models.py에 있는 Post를 import
#시험해본다..

admin.site.register(Post)