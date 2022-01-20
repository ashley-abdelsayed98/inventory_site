from django.urls import path

from .views import inventory_views, items_views, warehouses_views

urlpatterns = [
    path('', items_views.all_items, name='all_items'),
    path('items/', items_views.all_items, name='all_items'),
    path('items/<str:item_id>/', items_views.item, name='item'),
    path('items/<str:pk>/edit/', items_views.ItemUpdateView.as_view(), name='edit_item'),
    path('items/<str:pk>/delete/', items_views.ItemDeleteView.as_view(), name='delete_item'),
    path('warehouses/', warehouses_views.all_warehouses, name='all_warehouses'),
    path('warehouses/<str:pk>/', warehouses_views.WarehouseDetailView.as_view(), name='warehouse'),
    path('warehouses/<str:pk>/update/', warehouses_views.WarehouseUpdateView.as_view(), name='edit_warehouse'),
    path('warehouses/<str:pk>/delete/', warehouses_views.WarehouseDeleteView.as_view(), name='delete_warehouse'),
    path('new_inventory/<str:item_id>/', inventory_views.InventoryCreateView.as_view(), name='new_inventory'),
    path('edit_inventory/<int:pk>/', inventory_views.InventoryUpdateView.as_view(), name='edit_inventory'),
    path('delete_inventory/<int:pk>/', inventory_views.InventoryDeleteView.as_view(), name='delete_inventory'),
]