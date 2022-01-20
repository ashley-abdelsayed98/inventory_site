from django.contrib import admin
from .models import Product, Warehouse, WarehouseInventory

# Register your models here.

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(WarehouseInventory)