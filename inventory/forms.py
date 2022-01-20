from typing import Optional
from django import forms
from .models import Product, Warehouse, WarehouseInventory
from .crud import crud_product, crud_warehouse

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class WarehouseInventoryForm(forms.ModelForm):
    class Meta:
        model = WarehouseInventory
        fields = ['warehouse', 'stock']

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']
