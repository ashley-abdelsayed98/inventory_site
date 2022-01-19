from django.contrib import messages
from django.shortcuts import render, redirect

from ..crud import crud_warehouse
from ..forms import WarehouseForm


def warehouse(request, warehouse_id):
    warehouse = crud_warehouse.get_warehouse(id=warehouse_id)
    if request.POST.get('edit_warehouse'):       
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            warehouse_name = form.cleaned_data.get('name')
            warehouse_location = form.cleaned_data.get('location')
            crud_warehouse.update_warehouse(id= warehouse_id,name=warehouse_name, location=warehouse_location)
        else: 
            messages.error(request, "Warehouse name or location too long")
        return redirect('warehouse', warehouse_id=warehouse_id)
    elif request.POST.get('delete_warehouse'):
        crud_warehouse.delete_warehouse(id=warehouse_id)
        messages.success(request, f"Succesfully deleted warehouse: {warehouse.name}")
        return redirect('all_warehouses')
    else:
        form = WarehouseForm(instance=warehouse)
        context = { 
                    'warehouse': warehouse,
                    'form': form
                }
        return render(request=request, template_name="inventory/warehouse.html", context=context)

def all_warehouses(request):
    if request.method == 'POST':       
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse_name = form.cleaned_data.get('name')
            warehouse_location = form.cleaned_data.get('location')

            if crud_warehouse.get_warehouse_by_name(name=warehouse_name):
                messages.error(request, f"Warehouse '{warehouse_name}' already exists")
            else:
                crud_warehouse.create_warehouse(name=warehouse_name, location=warehouse_location)
                messages.success(request, f"Succesfully created warehouse {warehouse_name}")
        else:
            messages.error(request, "Warehouse name or location too long")
        return redirect('all_warehouses')
    else:
        form = WarehouseForm()
        warehouses = crud_warehouse.get_all_warehouses()
        context = {
                    'warehouses': warehouses,
                    'form': form    
                }
        return render(request=request, template_name="inventory/all_warehouses.html", context=context)
