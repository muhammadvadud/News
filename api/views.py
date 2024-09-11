from rest_framework import generics
from .serializers import ArticleSerializers, CommentSerializers, CategorySerializers, TagSerializers, \
    ArticleImageSerializers
from main.models import Article, Comment, Category, Tag, ArticleImage


class ArticleApiView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'slug'  # Slug orqali qidirish imkoniyati

    def get_queryset(self):
        slug = self.kwargs['slug']  # URL'dan slug qiymatini olish
        return Article.objects.filter(slug=slug)



class ArticleImageApiView(generics.CreateAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializers


class CommentApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
