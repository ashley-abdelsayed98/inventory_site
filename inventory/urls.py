from django.urls import path

from .views import inventory_views, items_views, warehouses_views

urlpatterns = [
    path('', items_views.all_items, name='all_items'),
    path('items/', items_views.all_items, name='all_items'),
    path('items/<str:item_id>/', items_views.item, name='item'),
    path('warehouses/', warehouses_views.all_warehouses, name='all_warehouses'),
    path('warehouses/<str:warehouse_id>/', warehouses_views.warehouse, name='warehouse'),
    path('new_inventory/<str:item_id>', inventory_views.new_inventory, name='new_inventory'),

]