from django.contrib import messages
from django.shortcuts import render, redirect

from ..crud import crud_item, crud_inventory
from ..forms import WarehouseInventoryForm


def new_inventory(request, item_id):
    item = crud_item.get_item(id=item_id)
    if request.method == 'POST':       
        form = WarehouseInventoryForm(request.POST)
        if form.is_valid():
            warehouse = form.cleaned_data.get('warehouse')
            stock = form.cleaned_data.get('stock')
            existing_inventory = crud_inventory.get_inventory_by_warehouse_and_item(item_id=item_id, warehouse_id=warehouse.id)
            if existing_inventory:
                if stock == 0:
                    crud_inventory.delete_warehouse_inventory(existing_inventory=existing_inventory)
                else:
                    crud_inventory.update_warehouse_inventory(id=existing_inventory.id, new_stock=stock+existing_inventory.stock)    
            else:
                if stock == 0:
                    messages.error(request, f"Cannot add inventory for item with 0 stock")
                else:
                    crud_inventory.create_inventory(item_id=item_id, warehouse_id=warehouse.id, stock=stock)
                    messages.success(request, f"Succesfully created additional inventory")
            return redirect(f'item', item_id)
        else:
            messages.error(request, f"Please enter a valid number of stock")
            return redirect(f"new_inventory", item_id)
    else:
        form = WarehouseInventoryForm()
        context = {
                    'item_name': item.name,
                    'form': form    
                }
        return render(request=request, template_name="inventory/new_inventory.html", context=context)