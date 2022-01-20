from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from ..crud import crud_item, crud_inventory
from ..models import WarehouseInventory


class InventoryCreateView(CreateView):
    model = WarehouseInventory
    template_name = 'inventory/new_inventory.html'
    fields = ['warehouse', 'stock']

    def form_valid(self, form):
        item_id = self.kwargs.get('item_id')
        item = crud_item.get_item(id=item_id)
        form.instance.item = item

        existing_stock = crud_inventory.get_inventory_by_warehouse_and_item(item_id=item_id, warehouse_id=form.instance.warehouse.id)
        if existing_stock:
            form.instance.id = existing_stock.id
            form.instance.stock = existing_stock.stock + form.instance.stock

        return super().form_valid(form)

class InventoryUpdateView(UpdateView):
    model = WarehouseInventory
    template_name = 'inventory/edit_inventory.html'
    fields = ['warehouse', 'stock']

class InventoryDeleteView(DeleteView):
    model = WarehouseInventory

    def get_success_url(self):
        item_id = self.get_object().item.id
        return reverse_lazy('item', kwargs={'item_id': item_id})
