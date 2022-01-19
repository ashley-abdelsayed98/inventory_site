
from django.contrib import messages
from django.shortcuts import render, redirect

from ..crud import crud_item, crud_warehouse, crud_inventory
from ..forms import ItemForm


def item(request, item_id):
    item = crud_item.get_item(id=item_id)
    stock = crud_inventory.get_all_inventory_by_item(item)
    if request.POST.get('edit_item'):       
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item_name = form.cleaned_data.get('name')
            item_description = form.cleaned_data.get('description')
            item_price = form.cleaned_data.get('price')

            if item_name != item.name and crud_item.get_item_by_name(item_name=item_name):
                messages.error(request, f"Item '{item_name}' already exists")
            if item_price < 0:
                messages.error(request, f"Price cannot be less than $0")
            else:
                crud_item.update_item(item=item, name=item_name, description=item_description, price=item_price)
                messages.success(request, f"Succesfully updated item {item_name}")
        return redirect('item', item_id=item.id)
    elif request.POST.get('delete_item'):
        crud_item.delete_item(item=item)
        messages.success(request, f"Succesfully deleted item: {item.name}")
        return redirect('all_items')
    elif request.POST.get('delete_inventory'):
        id = int(request.POST.get('delete_inventory'))
        crud_inventory.delete_warehouse_inventory(id=id)
        messages.success(request, f"Succesfully deleted inventory")
        return redirect('item', item_id=item.id)
    elif request.POST.get('edit_inventory'):
        id = int(request.POST.get('edit_inventory'))
        form = ItemForm(instance=item)
        context = { 
                    'item': item,
                    'available_stock':stock,
                    'form': form,
                    'editing_id': id
                }
        return render(request=request, template_name="inventory/item.html", context=context)
    elif request.POST.get('edit_inventory_confirm'):
        id = int(request.POST.get('edit_inventory_confirm'))
        new_stock = int(request.POST.get('edited_stock'))
        if new_stock == 0:
            crud_inventory.delete_warehouse_inventory(id=id)
        else:
            crud_inventory.update_warehouse_inventory(id=id, new_stock=new_stock)
        form = ItemForm(instance=item)
        context = { 
                    'item': item,
                    'available_stock':stock,
                    'form': form
                }
        return render(request=request, template_name="inventory/item.html", context=context)
    elif request.POST.get('edit_inventory_cancel'):
        form = ItemForm(instance=item)
        context = { 
                    'item': item,
                    'available_stock':stock,
                    'form': form
                }
        return render(request=request, template_name="inventory/item.html", context=context)
    elif request.POST.get('add_stock'):
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
