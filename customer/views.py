from django.views.generic import ListView
from django.shortcuts import render
from .models import Customer

def CustomerListView(request):
    customers = Customer.objects.all()
    return render(
        request, 
        'customers/customer_list.html', 
        {'customers': customers}
    )