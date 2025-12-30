from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from ..models import Customer, Sales
from ..forms import SalesForm


def list_view(request):
    """売上一覧ビュー"""
    sales_list = Sales.objects.select_related('customer', 'customer__pref', 'product').all()
    
    # 月別売上集計
    monthly_sales = Sales.objects.annotate(
        month=TruncMonth('sale_date')
    ).values('month').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-month')[:12]  # 直近12ヶ月
    
    # 顧客別売上集計（上位10件）
    customer_sales = Customer.objects.annotate(
        total=Sum('sales__amount'),
        count=Count('sales')
    ).filter(total__isnull=False).order_by('-total')[:10]
    
    # ページネーション
    paginator = Paginator(sales_list, 15)
    page_number = request.GET.get('page')
    sales = paginator.get_page(page_number)
    
    current_page = sales.number
    page_range = range(
        max(1, current_page - 3),
        min(paginator.num_pages + 1, current_page + 4)
    )
    
    return render(request, 'sales/list.html', {
        'sales': sales,
        'page_range': page_range,
        'monthly_sales': monthly_sales,
        'customer_sales': customer_sales,
    })


def create_view(request):
    """売上新規登録ビュー"""
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '売上を登録しました。')
            return redirect('customers:sales_list')
    else:
        form = SalesForm()
    
    return render(request, 'sales/create.html', {
        'form': form,
    })


def update_view(request, pk):
    """売上編集ビュー"""
    sale = get_object_or_404(Sales, pk=pk)
    
    if request.method == 'POST':
        form = SalesForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            messages.success(request, '売上情報を更新しました。')
            return redirect('customers:sales_list')
    else:
        form = SalesForm(instance=sale)
    
    return render(request, 'sales/edit.html', {
        'form': form,
        'sale': sale,
    })


def delete_view(request):
    """売上削除ビュー（複数選択対応）"""
    if request.method == 'POST':
        sales_ids = request.POST.getlist('sales_ids')
        
        if sales_ids:
            deleted_count = Sales.objects.filter(pk__in=sales_ids).delete()[0]
            messages.success(request, f'{deleted_count}件の売上を削除しました。')
        else:
            messages.warning(request, '削除する売上を選択してください。')
    
    return redirect('customers:sales_list')

