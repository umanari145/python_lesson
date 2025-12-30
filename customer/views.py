from django.views.generic import ListView
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
import pprint

def CustomerListView(request):
    """顧客一覧ビュー"""
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

def CustomerCreateView(request):
    """顧客新規登録ビュー"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '顧客を登録しました。')
            return redirect('customers:customer_list')
    else:
        form = CustomerForm()
    
    return render(request, 'customers/customer_create.html', {
        'form': form,
    })

def CustomerUpdateView(request, pk):
    """顧客編集ビュー"""
    # 編集対象の顧客を取得（存在しない場合は404エラー）
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        # 既存のインスタンスを渡してフォームを作成
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, '顧客情報を更新しました。')
            return redirect('customers:customer_list')
    else:
        # 既存のデータでフォームを初期化
        form = CustomerForm(instance=customer)
    
    return render(request, 'customers/customer_edit.html', {
        'form': form,
        'customer': customer,
    })