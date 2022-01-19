from django.db.models.fields import UUIDField
from ..models import Item

def create_item(name, description:str = None, price:float = None):
    new_item = Item(name=name, description=description, price=price)
    new_item.save()
    return

def get_all_items()->list[Item]:
    return Item.objects.all()

def get_item(id:int)->Item:
    return Item.objects.filter(id=id).first()

def get_item_by_name(item_name:str)->Item:
    return Item.objects.filter(name=item_name).first()

def update_item(item:Item, name:str, description:str = None, price:float = None)->None:
    item.name = name
    item.description = description
    item.price = price
    item.save()
    return

def delete_item(item:Item)->None:
    item.delete()
    return