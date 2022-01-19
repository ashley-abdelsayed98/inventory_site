from ..models import Warehouse

def create_warehouse(name:str, location:str = None)->None:
    new_warehouse = Warehouse(name=name, location=location)
    new_warehouse.save()
    return

def get_all_warehouses()->list[Warehouse]:
    return Warehouse.objects.all()

def get_warehouse(id:int)->Warehouse:
    return Warehouse.objects.filter(id=id).first()

def get_warehouse_by_name(name:str)->Warehouse:
    return Warehouse.objects.filter(name=name).first()

def update_warehouse(id, name, location:str = None)->None:
    warehouse = get_warehouse(id=id)
    warehouse.name = name
    warehouse.location = location
    warehouse.save()
    return

def delete_warehouse(id:int)->None:
    get_warehouse(id=id).delete()
    return