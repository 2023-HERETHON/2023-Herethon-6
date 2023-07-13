from django.contrib import admin
from .models import Post,Tag,Region,Category # Post 클래스를 사용하기 위해 models.py에 있는 Post를 import

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post)
admin.site.register(Tag, TagAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Category, CategoryAdmin)