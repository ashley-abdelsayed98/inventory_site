from typing import Optional
from django import forms
from .models import Item, Warehouse, WarehouseInventory
from .crud import crud_item, crud_warehouse

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']

class WarehouseInventoryForm(forms.ModelForm):
    class Meta:
        model = WarehouseInventory
        fields = ['warehouse', 'stock']

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']
