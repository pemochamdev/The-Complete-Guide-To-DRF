from django.contrib import admin

# Register your models here.

from news.models import Article, Journalist

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'title',  'location', 'publication_date', 'created_at', 'updated_at', 'is_active']
    #prepopulated_fields = {'slug':('title',)}
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
