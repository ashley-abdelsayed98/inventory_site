from ..models import Product, WarehouseInventory
from . import crud_product, crud_warehouse

def create_inventory(product_id, warehouse_id, stock)->None:
    new_warehouse = WarehouseInventory(product=crud_product.get_product(id=product_id), 
                                        warehouse=crud_warehouse.get_warehouse(id=warehouse_id), 
                                        stock=stock)
    new_warehouse.save()
    return

def get_inventory(id:int)->WarehouseInventory:
    return WarehouseInventory.objects.filter(id=id).first()

def get_inventory_by_warehouse_and_product(product_id:int, warehouse_id:int)->WarehouseInventory:
    return WarehouseInventory.objects.filter(product_id=product_id, warehouse_id = warehouse_id).first()

def get_all_inventory_by_product(product:Product)->list[WarehouseInventory]:
    return WarehouseInventory.objects.filter(product=product)

def update_warehouse_inventory(id:int, new_stock:int)->None:
    inventory = get_inventory(id)
    inventory.stock = new_stock
    inventory.save()
    return

def delete_warehouse_inventory(id=id)->None:
    get_inventory(id).delete()
    return