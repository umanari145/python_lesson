from django.urls import path
from .views import (
    list_view, create_view, update_view, delete_view,
    sales_list_view, sales_create_view, sales_update_view, sales_delete_view
)

app_name = 'customers'

urlpatterns = [
    # 顧客関連
    path('index/', list_view, name='customer_list'),
    path('create/', create_view, name='customer_create'),
    path('edit/<int:pk>/', update_view, name='customer_edit'),
    path('delete/', delete_view, name='customer_delete'),
    
    # 売上関連
    path('sales/', sales_list_view, name='sales_list'),
    path('sales/create/', sales_create_view, name='sales_create'),
    path('sales/edit/<int:pk>/', sales_update_view, name='sales_edit'),
    path('sales/delete/', sales_delete_view, name='sales_delete'),
]