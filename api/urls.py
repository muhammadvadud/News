from django.urls import path
from .views import ArticleApiView, ArticleDetailApiView, CategoryApiView, CommentApiView, TagApiView, \
    ArticleImageApiView

app_name = 'api'
urlpatterns = [
    path('article/', ArticleApiView.as_view(), name='article'),
    path('article-image/', ArticleImageApiView.as_view(), name='article_image'),
    path('comment/', CommentApiView.as_view(), name='comment'),
    path('category/', CategoryApiView.as_view(), name='category'),
    path('tag/', TagApiView.as_view(), name='tag'),
    path('<slug:slug>/', ArticleDetailApiView.as_view(), name='article_detail'),
]
