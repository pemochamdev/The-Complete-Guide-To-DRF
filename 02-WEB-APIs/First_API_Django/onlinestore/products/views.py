from django.shortcuts import render, get_object_or_404
from products.models import ManuFacturer, Product
from django.http import JsonResponse

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    data = {
        'products': list(products.values())#'pk', 'name', 'price'
    }
    response = JsonResponse(data)
    return response



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {
        'product':{
        'name': product.name,
        'manufacturer':product.manufacturer.name,
        'photo': product.photo.url,
        'description': product.description,
        'price':product.price,
        'shipping_cost': product.shipping_cost,
        'quantity': product.quantity
    }
    }
    response = JsonResponse(data)
    return response



def manufacturer_list(request):
    manufacturers = ManuFacturer.objects.filter(is_active=True)
    data = {
        'manufacturers': list(manufacturers.values())#'pk', 'name', 'price'
    }
    response = JsonResponse(data)
    return response



def manufactuer_detail(request, pk):
    manufacturer = get_object_or_404(ManuFacturer, pk=pk)
    manufacturer_products = manufacturer.products.all()
    data = {
        'manufacturer':{
        'name': manufacturer.name,
        'location':manufacturer.location,
        'is_active':manufacturer.is_active,
        'products': list(manufacturer_products.values())

        }
    }
    response = JsonResponse(data)
    return response





# from django.views.generic import DetailView, ListView, DeleteView
# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

# class ProductList(ListView)    :
#     model  = Product
#     template_name = 'products/product_list.html'