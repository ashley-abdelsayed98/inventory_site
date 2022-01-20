from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.FloatField(validators = [MinValueValidator(0.01)])
    def __str__(self):
        return f"Product : {self.name}"
    
    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'product_id': self.id})

class Warehouse(models.Model):
    name = models.CharField(unique=True, max_length=50)
    location = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}, Location: {self.location}"
    
    def get_absolute_url(self):
        return reverse_lazy('warehouse', kwargs={'pk': self.id})

class WarehouseInventory(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.CASCADE)
    stock = models.PositiveBigIntegerField(default=0)

    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={'product_id': self.product.id})
