from django.contrib import admin

# Register your models here.

from products.models import ManuFacturer, Product

@admin.register(ManuFacturer)
class ManuFacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'shipping_cost', 'quantity']

