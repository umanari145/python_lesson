from django.db import models
from django.db.models import Sum
from .prefecture import Prefecture


class Customer(models.Model):
    """顧客モデル"""
    customer_no = models.IntegerField(verbose_name='会員番号')
    name = models.CharField(max_length=20, verbose_name='名前')
    registered_date = models.DateField(verbose_name='登録日')
    pref = models.ForeignKey(
        Prefecture, 
        on_delete=models.PROTECT, 
        verbose_name='都道府県'
    )
    
    def __str__(self):
        return self.name
    
    def total_sales(self):
        """顧客の総売上金額を取得"""
        return self.sales.aggregate(total=Sum('amount'))['total'] or 0
    
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'
        ordering = ['customer_no']

