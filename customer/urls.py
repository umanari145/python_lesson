from django.urls import path
from .views import CustomerListView

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView, name='customer_list'),
]