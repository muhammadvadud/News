from rest_framework.serializers import ModelSerializer
from main.models import Category, Article, Tag, Comment, ArticleImage


class ArticleImageSerializers(ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['id', 'images', ]
        depth = 2


class ArticleSerializers(ModelSerializer):
    images = ArticleImageSerializers(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'content', 'slug', 'created_at', 'updated_at', 'category', 'tags', 'is_published', 'images']
        depth = 2


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        depth = 2


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
        depth = 2


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'name', 'last_name', 'content', 'created_at', 'updated_at']
        depth = 2
