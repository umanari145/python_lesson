from django.db import models
from .customer import Customer
from .product import Product


class Sales(models.Model):
    """売上モデル"""
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        related_name='sales',
        verbose_name='顧客'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='sales',
        verbose_name='商品'
    )
    sale_date = models.DateField(verbose_name='売上日')
    quantity = models.IntegerField(verbose_name='数量', default=1)
    unit_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name='単価',
        editable=False  # productの価格から自動でセットされるので手動編集不可
    )
    amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        verbose_name='金額',
        editable=False
    )
    
    def __str__(self):
        return f"{self.customer.name} - {self.product.name} ({self.sale_date})"
    
    def save(self, *args, **kwargs):
        """保存時に単価と金額を自動計算"""
        # 商品の単価を自動設定
        if self.product_id:
            self.unit_price = self.product.unit_price
        # 金額を計算
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = '売上'
        verbose_name_plural = '売上'
        ordering = ['-sale_date', '-id']

