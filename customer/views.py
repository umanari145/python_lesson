from django.views.generic import ListView
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render
from .models import Customer

def CustomerListView(request):
    customer_list = Customer.objects.all()
    # 1ページあたり10件
    paginator = Paginator(customer_list, 10)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
    
    # ページ番号のリストを作成（現在のページの前後3ページ）
    current_page = customers.number
    page_range = range(
        max(1, current_page - 3),
        min(paginator.num_pages + 1, current_page + 4)
    )
    
    return render(request, 'customers/customer_list.html', {
        'customers': customers,
        'page_range': page_range,
    })