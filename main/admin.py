from django.contrib import admin
from .models import Tag, Article, Comment, Category, ArticleImage

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Comment)
admin.site.register(Category)
