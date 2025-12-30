from django.urls import path
from .views import CustomerListView, CustomerCreateView

app_name = 'customers'

urlpatterns = [
    path('index/', CustomerListView, name='customer_list'),
    path('create/', CustomerCreateView, name='customer_create'),
]