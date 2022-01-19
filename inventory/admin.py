from django.contrib import admin
from .models import Item, Warehouse, WarehouseInventory

# Register your models here.

admin.site.register(Item)
admin.site.register(Warehouse)
admin.site.register(WarehouseInventory)