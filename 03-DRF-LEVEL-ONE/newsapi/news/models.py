from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Journalist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bibiography = models.TextField()

    def __str__(self):
        return f" {self.first_name} {self.last_name}"
    


class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete = models.CASCADE, related_name = 'articles')
    title = models.CharField(max_length = 50)
    slug = models.SlugField()
    description  = models.CharField(max_length=400)
    body  = models.TextField()
    location  = models.CharField(max_length=120)
    publication_date = models.DateField()

    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
    