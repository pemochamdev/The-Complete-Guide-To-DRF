from django.urls import path

from news.api import views

urlpatterns = [
    path('articles/', views.ArticleListCreateAPIView.as_view(), name="article_list"),
    path('articles/<pk>/', views.ArticleDetailApiView.as_view(), name="article_detail"),
    path('journalists/', views.JournalistListCreateAPIView.as_view(), name="journalist_list"),
    path('journalists/<pk>/', views.JournalistDetailApiView.as_view(), name="journalist_detail"),
#     path('articles/', views.article_list_create_api_view, name="article_list"),
#     path('articles/<pk>/', views.article_detail_api_view, name="article_detail"),
]
