from django.urls import path
from .views import list_view, create_view, update_view, delete_view

app_name = 'customers'

urlpatterns = [
    path('index/', list_view, name='customer_list'),
    path('create/', create_view, name='customer_create'),
    path('edit/<int:pk>/', update_view, name='customer_edit'),
    path('delete/', delete_view, name='customer_delete'),
]