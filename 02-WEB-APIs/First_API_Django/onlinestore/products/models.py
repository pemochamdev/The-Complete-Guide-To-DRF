from django.db import models

# Create your models here.


class ManuFacturer(models.Model):
    name = models.CharField(max_length=200)
    location  = models.CharField(max_length=400)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(ManuFacturer, on_delete=models.CASCADE, related_name = 'products')
    name = models.CharField(max_length = 200)
    description  = models.TextField()
    photo = models.ImageField(upload_to='photos/products')
    price = models.FloatField(default = 0.0)
    shipping_cost = models.FloatField()
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
    