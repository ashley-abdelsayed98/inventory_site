
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from ..crud import crud_product, crud_inventory, crud_warehouse
from ..forms import ProductForm
from ..models import Product


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'inventory/edit_product.html'
    fields = ['name', 'description', 'price']

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('all_products')

def product(request, product_id):
    product = crud_product.get_product(id=product_id)
    stock = crud_inventory.get_all_inventory_by_product(product)
    if request.POST.get('add_stock'):
        if not crud_warehouse.get_all_warehouses():
            messages.error(request, f"Please add a warehouse before adding stock")
            return redirect(f'product', product_id)
        else:
            return redirect('new_inventory', product_id)
    else:
        form = ProductForm(instance=product)
        context = { 
                    'product': product,
                    'available_stock':stock,
                    'form': form
                }
        return render(request=request, template_name="inventory/product.html", context=context)

def all_products(request):
    if request.method == 'POST':       
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('name')
            product_description = form.cleaned_data.get('description')
            product_price = form.cleaned_data.get('price')
            crud_product.create_product(name=product_name, description=product_description, price=product_price)
            messages.success(request, f"Succesfully created product {product_name}")
        else: 
            messages.error(request, "Please ensure your product has a unique name and price greater than $0")
        return redirect('all_products')
    else:
        form = ProductForm()
        products = crud_product.get_all_products()
        context = {
                    'products': products,
                    'form': form    
                }
        return render(request=request, template_name="inventory/all_products.html", context=context)
