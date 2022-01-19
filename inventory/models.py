from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    def __str__(self):
        return f"Item : {self.name}"

class Warehouse(models.Model):
    name = models.CharField(unique=True, max_length=50)
    location = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}, Location: {self.location}"

class WarehouseInventory(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(to=Warehouse, on_delete=models.CASCADE)
    stock = models.PositiveBigIntegerField(default=0)