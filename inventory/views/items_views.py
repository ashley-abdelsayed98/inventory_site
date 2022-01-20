
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from ..crud import crud_item, crud_inventory, crud_warehouse
from ..forms import ItemForm
from ..models import Item


class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'inventory/edit_item.html'
    fields = ['name', 'description', 'price']

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('all_items')

def item(request, item_id):
    item = crud_item.get_item(id=item_id)
    stock = crud_inventory.get_all_inventory_by_item(item)
    if request.POST.get('add_stock'):
        if not crud_warehouse.get_all_warehouses():
            messages.error(request, f"Please add a warehouse before adding stock")
            return redirect(f'item', item_id)
        else:
            return redirect('new_inventory', item_id)
    else:
        form = ItemForm(instance=item)
        context = { 
                    'item': item,
                    'available_stock':stock,
                    'form': form
                }
        return render(request=request, template_name="inventory/item.html", context=context)

def all_items(request):
    if request.method == 'POST':       
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data.get('name')
            item_description = form.cleaned_data.get('description')
            item_price = form.cleaned_data.get('price')
            crud_item.create_item(name=item_name, description=item_description, price=item_price)
            messages.success(request, f"Succesfully created item {item_name}")
        else: 
            messages.error(request, "Please ensure your item has a unique name and price greater than $0")
        return redirect('all_items')
    else:
        form = ItemForm()
        items = crud_item.get_all_items()
        context = {
                    'items': items,
                    'form': form    
                }
        return render(request=request, template_name="inventory/all_items.html", context=context)
