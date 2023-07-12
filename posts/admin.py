from django.contrib import admin
from .models import Post # Post 클래스를 사용하기 위해 models.py에 있는 Post를 import

admin.site.register(Post)