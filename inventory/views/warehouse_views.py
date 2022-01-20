from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView

from ..crud import crud_warehouse
from ..forms import WarehouseForm
from ..models import Warehouse


class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = 'inventory/warehouse.html'

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    template_name = 'inventory/edit_warehouse.html'
    fields = ['name', 'location']

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('all_warehouses')

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
