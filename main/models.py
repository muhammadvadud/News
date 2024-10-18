from django.db import models
from django.utils.text import slugify


# Kategoriya modeli
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Teglar modeli
class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Maqola modeli
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='articles')
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/" + str(self.slug) + "/"

    class Meta:
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images',on_delete=models.CASCADE)  # ForeignKey orqali bog'lanish
    images = models.ImageField(upload_to='article_image/', null=True, blank=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"
