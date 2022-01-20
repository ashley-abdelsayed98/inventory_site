from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from ..crud import crud_product, crud_inventory
from ..models import WarehouseInventory


# Create Inventory, Inventory holds the amount of stock of a product at a certain warehouse
class InventoryCreateView(CreateView):
    model = WarehouseInventory
    template_name = 'inventory/new_inventory.html'
    fields = ['warehouse', 'stock']

    def form_valid(self, form):
        product_id = self.kwargs.get('product_id')
        product = crud_product.get_product(id=product_id)
        form.instance.product = product

        existing_stock = crud_inventory.get_inventory_by_warehouse_and_product(product_id=product_id, warehouse_id=form.instance.warehouse.id)
        if existing_stock:
            form.instance.id = existing_stock.id
            form.instance.stock = existing_stock.stock + form.instance.stock

        return super().form_valid(form)

# Update the stock of a product at a certain warehouse
class InventoryUpdateView(UpdateView):
    model = WarehouseInventory
    template_name = 'inventory/edit_inventory.html'
    fields = ['warehouse', 'stock']

# Delete stock of a product at a certain warehouse
class InventoryDeleteView(DeleteView):
    model = WarehouseInventory

    def get_success_url(self):
        product_id = self.get_object().product.id
        return reverse_lazy('product', kwargs={'product_id': product_id})
