from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView

app_name = 'customers'

urlpatterns = [
    path('index/', CustomerListView, name='customer_list'),
    path('create/', CustomerCreateView, name='customer_create'),
    path('edit/<int:pk>/', CustomerUpdateView, name='customer_edit'),
]