from ..models import Product

def create_product(name, description:str = None, price:float = None):
    new_product = Product(name=name, description=description, price=price)
    new_product.save()
    return

def get_all_products()->list[Product]:
    return Product.objects.all()

def get_product(id:int)->Product:
    return Product.objects.filter(id=id).first()

def get_product_by_name(product_name:str)->Product:
    return Product.objects.filter(name=product_name).first()

def update_product(product:Product, name:str, description:str = None, price:float = None)->None:
    product.name = name
    product.description = description
    product.price = price
    product.save()
    return

def delete_product(product:Product)->None:
    product.delete()
    return