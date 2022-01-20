from django.urls import path

from .views import inventory_views, product_views, warehouse_views

urlpatterns = [
    path('', product_views.all_products, name='all_products'),
    path('products/', product_views.all_products, name='all_products'),
    path('products/<str:product_id>/', product_views.product, name='product'),
    path('products/<str:pk>/edit/', product_views.ProductUpdateView.as_view(), name='edit_product'),
    path('products/<str:pk>/delete/', product_views.ProductDeleteView.as_view(), name='delete_product'),
    path('warehouses/', warehouse_views.all_warehouses, name='all_warehouses'),
    path('warehouses/<str:pk>/', warehouse_views.WarehouseDetailView.as_view(), name='warehouse'),
    path('warehouses/<str:pk>/update/', warehouse_views.WarehouseUpdateView.as_view(), name='edit_warehouse'),
    path('warehouses/<str:pk>/delete/', warehouse_views.WarehouseDeleteView.as_view(), name='delete_warehouse'),
    path('new_inventory/<str:product_id>/', inventory_views.InventoryCreateView.as_view(), name='new_inventory'),
    path('edit_inventory/<int:pk>/', inventory_views.InventoryUpdateView.as_view(), name='edit_inventory'),
    path('delete_inventory/<int:pk>/', inventory_views.InventoryDeleteView.as_view(), name='delete_inventory'),
]