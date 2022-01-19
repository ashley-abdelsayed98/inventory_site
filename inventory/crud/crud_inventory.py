from ..models import Item, WarehouseInventory
from . import crud_item, crud_warehouse

def create_inventory(item_id, warehouse_id, stock)->None:
    new_warehouse = WarehouseInventory(item=crud_item.get_item(id=item_id), 
                                        warehouse=crud_warehouse.get_warehouse(id=warehouse_id), 
                                        stock=stock)
    new_warehouse.save()
    return

def get_inventory(id:int)->WarehouseInventory:
    return WarehouseInventory.objects.filter(id=id).first()

def get_inventory_by_warehouse_and_item(item_id:int, warehouse_id:int)->WarehouseInventory:
    return WarehouseInventory.objects.filter(item_id=item_id, warehouse_id = warehouse_id).first()

def get_all_inventory_by_item(item:Item)->list[WarehouseInventory]:
    return WarehouseInventory.objects.filter(item=item)

def get_warehouse(name:str)->WarehouseInventory:
    return WarehouseInventory.objects.filter(name=name).first()

def update_warehouse_inventory(id:int, new_stock:int)->None:
    inventory = get_inventory(id)
    inventory.stock = new_stock
    inventory.save()
    return

def delete_warehouse_inventory(id=id)->None:
    get_inventory(id).delete()
    return