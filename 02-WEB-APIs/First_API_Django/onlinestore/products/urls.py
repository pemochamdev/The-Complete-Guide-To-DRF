from django.urls import path

from products import views

urlpatterns = [
    #path('', views.ProductList.as_view(), name='product_list'),
    #path('', views.ProductDetail.as_view(), name='product_detail'), 
    path('products/', views.product_list, name='product_list'),
    path('products/<pk>/', views.product_detail, name='product_detail'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer_list'),
    path('manufacturers/<pk>/', views.manufactuer_detail, name='manufacturer_detail'),
]
